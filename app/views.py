import csv
import os
import io
import threading
from rest_framework import generics
from .models import Client, Product, Bill
from .serializers import ClientSerializer, ProductSerializer, BillSerializer, CSVClientSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from asgiref.sync import sync_to_async


def generate_csv(file_name):
    clients = Client.objects.all()
    data = []

    for client in clients:
        num_bills = client.bill_set.count()
        serializer = CSVClientSerializer({'document': client.document, 'full_name': client.first_name, 'num_bills': num_bills})
        data.append(serializer.data)

    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['document', 'full_name', 'num_bills']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    return file_name

@api_view(['GET'])
def generate_csv_async(request):
    file_name = 'clients_' + datetime.now().strftime('%Y%m%d_%H%M%S%f') + '.csv'
    threading.Thread(target=generate_csv, args=(file_name,)).start()
    return JsonResponse({"file_name": file_name})


@api_view(['GET'])
def download_csv(request):
    file_name = request.GET.get('file_name', '')
    if file_name and os.path.exists(file_name):
        with open(file_name, 'rb') as csvfile:
            response = HttpResponse(csvfile.read(), content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={file_name}'
        os.remove(file_name)
        return response
    else:
        return JsonResponse({"comments": "El archivo no está disponible o el nombre es incorrecto. Intenta generar el CSV primero."})
    
@api_view(['POST'])
def upload_csv(request):
    if 'file' not in request.FILES:
        return JsonResponse({"error": "No se proporcionó un archivo CSV."}, status=400)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        return JsonResponse({"error": "El archivo proporcionado no es un archivo CSV válido."}, status=400)

    clients_data = []
    try:
        csv_file_wrapper = io.TextIOWrapper(csv_file.file, encoding='utf-8')
        reader = csv.DictReader(csv_file_wrapper)
        for row in reader:
            clients_data.append(row)
    except Exception as e:
        return JsonResponse({"error": f"No se pudo leer el archivo CSV. Error: {str(e)}"}, status=400)

    threading.Thread(target=async_create_clients, args=(clients_data,)).start()

    return JsonResponse({"message": "Carga masiva en proceso. Verifica el estado más tarde."})


def async_create_clients(clients_data):
    for data in clients_data:
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(f"Error de validación: {serializer.errors}")

    print("Proceso de creación masiva completado.")
    from django.db import connections
    connections.close_all()
 

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
