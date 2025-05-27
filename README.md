## Folder and File Structure

```
django-api/
│
├── django-api/                 # Django Project Root
│   ├── __init__.py
│   ├── settings.py             # Settings for the entire project
│   ├── urls.py                 # Project-level URL configuration
│   ├── wsgi.py                 # WSGI entry point
│   ├── asgi.py                 # ASGI entry point (if using async)
│   └── manage.py               # Command-line utility for the project
│
├── apps/
│   ├── users/                  # App for handling user accounts
│   │   ├── migrations/         # Migration files for database changes
│   │   ├── __init__.py
│   │   ├── models.py           # User models
│   │   ├── serializers.py      # User serializers
│   │   ├── views.py            # User views (authentication, registration, etc.)
│   │   ├── urls.py             # URLs related to user actions
│   │   ├── permissions.py      # User permissions (admin, customer)
│   │   └── admin.py            # Register user model to Django admin
│
│   ├── products/               # App for managing products
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py           # Models for Product, Category, etc.
│   │   ├── serializers.py      # Serializers for transforming models into JSON
│   │   ├── views.py            # Product views for listing, creating, etc.
│   │   ├── urls.py             # URLs related to product actions
│   │   └── admin.py            # Register product and category models to Django admin
│
│   ├── orders/                 # App for managing orders
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py           # Models for Order, OrderItems
│   │   ├── serializers.py      # Order serializers
│   │   ├── views.py            # Views to handle order placement, status tracking, etc.
│   │   ├── urls.py             # URLs related to orders
│   │   └── admin.py            # Register order models to Django admin
│
│   ├── payments/               # App for handling payment processing
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py           # Models for Payment, Transaction, etc.
│   │   ├── serializers.py      # Payment serializers
│   │   ├── views.py            # Views for handling payments
│   │   ├── urls.py             # URLs related to payments
│   │   └── admin.py            # Register payment models to Django admin
│
│   ├── cart/                   # App for managing shopping cart
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── models.py           # Models for Cart, CartItems
│   │   ├── serializers.py      # Cart serializers
│   │   ├── views.py            # Views to handle cart-related actions (add, remove, update)
│   │   ├── urls.py             # URLs related to cart
│   │   └── admin.py            # Register cart models to Django admin
│
├── env/                        # Virtual environment for Python dependencies (if using)
├── .gitignore                  # Git ignore file (to avoid committing unnecessary files)
├── requirements.txt            # List of Python dependencies
├── README.md                   # Documentation for your project
```

## Installation

**1.Cloning the Repository**

```sh
$ git clone https://github.com/TrungDN1996/django-api.git

$ cd django_api
```

**2.Installing the environment control**

```sh
$ python -m venv env

```

**3.Activating the environment**

on Windows:
```sh
env\Scripts\activate

```
on Mac OS / Linux:
```sh
$ source env/bin/activate

```

**4.Installing dependencies**

```sh
$ pip install -r requirements.txt

```

**5.Last commands to start**

```sh
$ python manage.py makemigrations

$ python manage.py migrate

```
**6.Create a super user**

```sh
$ python manage.py createsuperuser admin-name

```

**7.Finishing running server**

```sh
$ python manage.py runserver

```