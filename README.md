# API para el Control de Clientes, Facturas y Productos
Esta API permite gestionar operaciones CRUD en entidades como Clientes, Facturas y Productos. Además, ofrece funcionalidades adicionales como autenticación de usuarios, generación asincrónica de exportables CSV y cargue masivo de datos desde archivos CSV.

### Instalación 🔧
Sigue estos pasos para instalar y ejecutar la API en tu entorno local:

_Clonación del repositorio_

```shell
git clone git@github.com:dickson7/api-clients-bills-products.git
````
_Ingresamos en el directorio del repositorio clonado, y ejecutamos el siguiente comando para habilitar el entorno virtual_

```shell
python3 -m venv env
```

_Activamos el entorno virtual_

```shell
source env/bin/activate
```

_Instalamos las dependencias con pip_

```shell
(env)$ pip3 install -r requirements.txt
```

_Lanzamos migraciones_

```shell
(env)$ python3 manage.py makemigrations
(env)$ python3 manage.py migrate
```


_Como último paso realizamos la ejecución del servidor_

```shell
(env)$ python3 manage.py runserver
```

### Uso 🚀
Después de completar la instalación y ejecutar el servidor, puedes acceder a la documentación de los endpoints visitando la dirección raíz de la API. La documentación completa está disponible a través de Swagger.

Es importante destacar que la API utiliza un sistema de autorización basado en tokens JWT (JSON Web Tokens). Para interactuar con los endpoints protegidos, primero debes registrarte en la API utilizando el endpoint de registro e iniciar sesión. Esto te proporcionará un token de acceso que debes incluir en las solicitudes a los endpoints protegidos.

Una vez que tengas un token válido, podrás gestionar clientes, facturas y productos. Los endpoints están diseñados para proporcionar una gestión eficiente de estos elementos.

Asegúrate de incluir el token de acceso en la cabecera de autorización de cada solicitud protegida, utilizando el formato 'Bearer '. Esto permitirá que la API verifique tu identidad y autorice tus acciones de acuerdo con los permisos asociados a tu cuenta.

Explora la documentación detallada de la API para obtener más información sobre los diferentes endpoints disponibles, los parámetros requeridos, los tipos de respuesta y las operaciones compatibles. ¡Disfruta de la experiencia de gestión de clientes, facturas y productos de forma segura y eficiente a través de nuestra API!

![Swgger ](/Swagger%20-%20API%20de%20Clientes,%20Facturas%20y%20Productos.png)