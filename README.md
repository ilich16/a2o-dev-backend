# A2O Backend

Project made with Django that contains the backend server for the React App.

## Setup

This project can use [pipenv](https://github.com/pypa/pipenv) or [pip](https://pip.pypa.io/en/stable/) as package manager.

Using [pipenv](https://github.com/pypa/pipenv):

```bash
pipenv install
```

Using [pip](https://pip.pypa.io/en/stable/):
```bash
pip install Django==3.1.4
pip install django-cors-headers
```

## Usage

Run the backend server.

```bash
python manage.py runserver
```

The API will be able to access at `http://localhost:8000/`.