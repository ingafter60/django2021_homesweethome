# django2021_homesweethome
Membuat Aplikasi HomeSweetHome ala AirBnB menggunakan Django v.2.2.5
https://github.com/ingafter60/django2021_homesweethome

# Om Ang Namah: Hamba ingin menyelesaikan proyek ini, mohon tuntunan-Mu

## STAY FOCUS 2021

### Initial commit - Creating github repository

        modified:   README.md

### Membuat django proyek 'config'

        # Membuat virtual environment menggunakan python v3
        > pipenv --three
        # Actifkan pipenv
        > pipenv shell
        # Install django v2.2.5
        > pipenv install django==2.2.5
        # Membuat django proyek
        > django-admin startproject config .
        # Jalankan server untuk mengujinya
        > python manage.py runserver
        ...
        Starting development server at http://127.0.0.1:8000/
        .
        ├── LICENSE
        ├── Pipfile
        ├── Pipfile.lock
        ├── README.md
        ├── config
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3
        └── manage.py
        modified:   README.md

### Database - Setting up postgres for the db

        # Jalankan postgres server
        > sudo service postgresql start
        # Gunakan postgres untuk membuat db
        > sudo -u postgres psql
        # Buat database
        > postgres=# CREATE DATABASE django2021_homesweethome;
        CREATE DATABASE
        # Membuat user baru + password
        > postgres=# CREATE USER user2021 WITH PASSWORD '2021';
        CREATE ROLE
        # Grant All Privileges
        > postgres=# GRANT ALL PRIVILEGES ON DATABASE django2021_homesweethome TO user2021;
        GRANT
        # Uji hasilnya
        postgres=# \l
        ...
        django2021_homesweethome
        modified:   README.md

###	Modified README.md 

### Koneksi - Hubungan database dengan django proyek

        modified:   README.md
        # Install psycopg2 postgres driver
        > pipenv instll psycopg2
        # Setup db pada settings files
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'django2021_homesweethome', 
                'USER': 'user2021', 
                'PASSWORD': '2021',
                'HOST': '127.0.0.1', 
                'PORT': '5432',
            }
        }
        # Djalankan server untuk mengujinya
        > python manage.py runserver
        ...
        Starting development server at http://127.0.0.1:8000/
        :)

### App - Membuat app baru 'users' dan mencatatkannya pada proyek

        modified:   README.md
        # Membuat app 'users'
        > django-admin startapp users
        # Catatkan users pada settings file
        .
        ├── LICENSE
        ├── Pipfile
        ├── Pipfile.lock
        ├── README.md
        ├── config
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3
        ├── manage.py
        └── users
            ├── __init__.py
            ├── admin.py
            ├── apps.py
            ├── migrations
            │   └── __init__.py
            ├── models.py
            ├── tests.py
            └── views.py      

### Auth - Membuat User auth menggunakan Django AbstractUser

        # USERS/models.py
        from django.contrib.auth.models import AbstractUser
        from django.db import models
        class User(AbstractUser):
           pass

        # USERS/admin.py
        from django.contrib import admin
        from . import models

        # Register your models here.
        admin.site.register(models.User)

        # new
        AUTH_USER_MODEL = 'users.User'

        > python manage.py makemigrations
        > python manage.py migrate
        > python manage.py createsuperuser

        modified:   README.md
        modified:   config/settings.py
        modified:   users/admin.py
        new file:   users/migrations/0001_initial.py
        modified:   users/models.py
        :)

### Kolom - Menambah kolom 'avatar dan gender' pada Users table/model 

        modified:   Pipfile
        modified:   Pipfile.lock
        modified:   README.md
        modified:   users/admin.py
        new file:   users/migrations/0002_user_bio.py
        new file:   users/migrations/0003_auto_20210102_0232.py
        modified:   users/models.py
























































































































