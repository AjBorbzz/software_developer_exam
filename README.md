# software developer exam

  - Project done in Django version 3.0.2

Features:
  - Responsive Web Design
  - toggable side bear menu (Hide/Show side bar menu)
  - Used Twitter Bootstrap & Crispy form
  - JQuery UI (for draggable and sortable data)
  - HTML5 (DRY Principles)
  - Django MVC with OOP coding convention

### Pages

Home page:

* Displays draggable and sortable database in table.
* Data can be filtered via car_color : 'Red' and 'Blue'

Enroll Car page:
* Enroll car page has 4 fields to fill-up: Car Brand, Car Model, Car Owner, Car Color.
* When button "Submit" is clicked, the user will be redirected to Home page with an updated table.

Instruction page:
* Contains the problem and constraints of the software developer exam.

### Installation

requires [Django](https://www.djangoproject.com/download/) v3.0.2 to run.

Install the dependencies and  and start the server.

```sh
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install django
$ pip install django-bootstrap4
$ pip install django-crispy-forms
```


### Run Migration

```sh
$ cd valens_cars
$ python manage.py makemigrations
$ python manage.py migrate
```

### Run Localhost

current directory should be in valens_cars/
```sh
$ python manage.py runserver 
```

### Admin
Username : admin
Password: password

### Other info
```gitignore file
### Django ###
*.log
*.pot
*.pyc
__pycache__/
local_settings.py
db.sqlite3
/media
virtual
/static
```
