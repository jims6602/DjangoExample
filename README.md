# DjangoExample

# References     
* [Django and MS SQL Server 2012 Connection (2018) - by Royce Chue](https://medium.com/@royce236/django-and-ms-sql-server-2012-connection-2018-120c54dfc037)


# Environment

## Add SQL Server driver
```
pip install django-pyodbc-azure
```

## Create Environment 
```
C:\env1>  virtualenv . -p C:\\Python36\\python
```

## Activate Environment
```
C:\env1>./Scripts/activate
```

## Install Django 
```
(env1) PS C:env1\>pip install django==2.0.7
```

## Check Environment for versions
```
(env1) PS C:\env1>pip freeze
Django==2.0.7
pytz==2019.3
```
# Project

## Create New Django Project
```
(env1) PS C:\env1> mkdir scr
(env1) PS C:\env1> cd scr

(env1) PS C:\env1\scr>django-admin startproject <project-name>
```

## Start Web Server
```
(env1) PS C:\env1> cd <project-name>
(env1) PS C:\env1\ <project-name> > python manage.py runserver
```

## Make Migrations
 Which is responsible for creating new migrations based on the changes you have made to your models.
```
(env1) PS C:\env1\ <project-name> > python manage.py makemigrations
Migrations for 'products':
  products\migrations\0001_initial.py
    - Create model Product
```

## Migration 
Which is responsible for applying and unapplying migrations.
```
(env1) PS C:\env1\ <project-name> > python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, products, sessions
Running migrations:
  Applying products.0001_initial... OK
```

## Setting administration User
URL: http://127.0.0.1:8000/admin/
```
(env1) PS C:\env1\ <project-name> > python manage.py createsuperuser
Username (leave blank to use 'johncusey'): john
Email address: jjcusey@gmail.com
Password:
Password (again):
Superuser created successfully.
```

## Create App Components   
```
(env1) PS C:\env1\ <project-name> > python manage.py startapp <components-name>
```  

# Python Shell    

## Accessing the shell
```
(evn1) PS C:\env1\ <project-name> > python manage.py shell  
Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```  

## Initialize Object    
```
>>> from products.models import Product

>>> Product.objects.all()
<QuerySet [<Product: Product object (1)>]>
```

## New Object    
```
>>> Product.objects.create(title='Truck', description='Item that moves dirty', price='$10.00')
<Product: Product object (2)>
```
