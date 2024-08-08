from django.shortcuts import render
from django.http import JsonResponse
import json
from .text import dictionary


def index(request):
    return render(request, 'index.html')


def get_value_for_key(key):
    return dictionary.get(key, "Значение не найдено")


def get_value(request):
    if request.method == 'POST':
        keys = json.loads(request.POST.get('keys'))
        values = [get_value_for_key(key) for key in keys]
        return JsonResponse({'values': values})


def get_keys(request):
    keys = list(dictionary.keys())
    return JsonResponse({'keys': keys})
