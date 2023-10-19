from django.shortcuts import render

from .models import Greeting

def index(request):
     return render(request, 'index.html')

def cronograma1(request):
     return render(request, 'cronograma1.html')

def cronograma2(request):
     return render(request, 'cronograma2.html')

def materiais(request):
     return render(request, 'materiais.html')

def relatorios(request):
     return render(request, 'relatorios.html')

def dashboard(request):
     return render(request, 'dashboard.html')


def db(request):
    # If you encounter errors visiting the `/db/` page on the example app, check that:
    #
    # When running the app on Heroku:
    #   1. You have added the Postgres database to your app.
    #   2. You have uncommented the `psycopg` dependency in `requirements.txt`, and the `release`
    #      process entry in `Procfile`, git committed your changes and re-deployed the app.
    #
    # When running the app locally:
    #   1. You have run `./manage.py migrate` to create the `hello_greeting` database table.

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
