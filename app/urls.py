from django.urls import path
from .views import (
    ClientListCreateView, ClientDetailView,
    ProductListCreateView, ProductDetailView,
    BillListCreateView, BillDetailView, generate_csv_async, download_csv, upload_csv
)

urlpatterns = [
    # Clients
    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),

    # Products
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    # Bills
    path('bills/', BillListCreateView.as_view(), name='bill-list'),
    path('bills/<int:pk>/', BillDetailView.as_view(), name='bill-detail'),
    
    # Generate CSV
    path('generate-csv/', generate_csv_async, name='generate-csv'),
    path('validate-csv/', download_csv, name='validate-csv'),
    path('upload-csv/', upload_csv, name='upload-csv'),
]