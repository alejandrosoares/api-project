# API Project

## Comandos:

- Ejecutar Celery
```
celery -A api.celery worker -l info -Q populate_db
```
- Ejecutar redis server
```
redis-server
``` 

## Pasos realizados:


### 1. Creaci&oacute;n de los modelos
- An&aacute;lisis del endpoint.

El an&aacute;lisis de los datos provistos por el endpoint se realiz&oacute; mediante el script <b>api/verify_data.py</b>.
Con ello se determino el max_length de los campos de texto.
Adem&aacute;s tambi&eacute;n se observ&oacute; los valores de los siguientes campo: 

Campo 'Auth':
['apiKey', '', 'OAuth', 'X-Mashape-Key', 'User-Agent']

Campo 'Cors':
['yes', 'no', 'unknown']

Si bien se dedicidi&oacute; dejar estos campos como CharField, tambi&eacute;n se podrian haber registrado como un campo PositiveSmallIntegerField con el argumento de palabra clave choices.
Esto traeria un ahorro en de espacio en memoria pero aumentaria tiempo de ejecuci&oacute;n para pasar el valor numerico a 
el valor del string.


- Creaci&oacute;n de los modelos Category y Api.

### 2.Configuracion del Celery
Configuraci&oacute;n celery y redis como message broker. Ejecuci&oacute;n del servidor de redis

### 4.Creaci&oacute;n de la funcionalidad <b>PopulateDB</b>
- Creaci&oacute;n de PopulateSerializer.
- Creaci&oacute;n de la funci&oacute;n asyncrona populate_db.
- Creaci&oacute;n de la vista PopulateView y las urls.
- Comprobaci&oacute;n de su funcionamiento.

### 6. Creaci&oacute;n de la funcionalidad <b>search by keyword</b>
- Creaci&oacute;n de ApiSerializer.
- Creaci&oacute;n de la vista SearchByIdView y las urls.
- Comprobaci&oacute;n de su funcionamiento.

### 7. Creaci&oacute;n de la funcionalidad <b>search by category</b>
- Creaci&oacute;n de la vista SearchByCategoryView y las urls.
- Comprobaci&oacute;n de su funcionamiento.

### 8. Creaci&oacute;n de la funcionalidad <b>ordened list</b>
- Creaci&oacute;n de la vista OrdenedListView y las urls.
- Comprobaci&oacute;n de su funcionamiento.

### 9. Creaci&oacute;n de la funci&oacute;n <b>search item</b>
- Creaci&oacute;n de la vista ItemView y las urls
- Comprobaci&oacute;n de su funcionamiento.

Las comprobaciones del funcionamiento de las vistas se realiz&oacute; mediante la aplicaci&oacute;n Insomnia, del cual se
deja el archivo <b>api/insomnia.json</b> para poder importar dentro de la aplicaci&oacute;n y
poder verficar el funcionamiento de las vistas.


### 10. Realizaci&oacute;n de los TestView
Se realizaron los test para cada vista.
Los test se puede correr mediante:
```
python3 manage.py test
```