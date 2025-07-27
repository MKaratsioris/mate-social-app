# Useful Commands for Django

## First setup
- `djprj = django-admin startproject mate`
- `djdb = python3 manage.py makemigrations && python3 manage.py migrate`
    - `djmk = python3 manage.py makemigrations`
    - `djmg = python3 manage.py migrate`
- `djsu = python3 manage.py createsuperuser`
- `djrs = python3 manage.py runserver`

## Setup of New App, i.e. todo
- `cd mate/`
- `djapp todo = django-admin startapp todo`
- In `mate/mate/settings.py`, add `apps.todo`in the `INSTALLED_APPS` list.
- In `mate/apps/todo/apps.py`, add `TodoConfig.name = 'apps.todo'`
- In `mate/mate/urls.py`, add `path('todo/', include('todo.urls')),` in the `urlpatterns` list.
- `djrs`

## Upgrade to latest
- `pip install django --upgrade`