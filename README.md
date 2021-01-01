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




































































































































