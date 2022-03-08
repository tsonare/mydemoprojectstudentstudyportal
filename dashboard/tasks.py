from django.http import HttpResponse
from celery import shared_task
import wikipedia
from .forms import *


@shared_task
def add(x, y):
    return x + y


@shared_task
def multi(x, y):
    return x * y


@shared_task
def search_wikipedia(search):
    result = wikipedia.page(search)

    # result = wikipedia.summary(search, sentences=100)
    return result
