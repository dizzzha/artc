from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .output_dict import dictionary
from .output_dict2 import dictionary as dict2


def index(request):
    return render(request, 'index.html')


def second_floor(request):
    return render(request, 'second_floor.html')


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


def get_values(request):
    values = [value[1] for value in dictionary.values()]
    return JsonResponse({'values': values})


def get_keys2(request):
    keys = list(dict2.keys())
    return JsonResponse({'keys': keys})


def get_values2(request):
    values = [value[1] for value in dict2.values()]
    return JsonResponse({'values': values})


@csrf_exempt
def search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        search_values = data.get('search_values', [])

        results = []
        for search_value in search_values:
            key_result = dictionary.get(search_value) or dictionary.get(search_value.upper()) or dictionary.get(
                search_value.lower())

            value_results = [
                (key, value) for key, value in dictionary.items()
                if search_value.lower() == value[1].lower()
            ]

            if key_result:
                results.append({
                    'key': search_value,
                    'value1': key_result[0],
                    'value2': key_result[1]
                })
            elif value_results:
                for key, value in value_results:
                    results.append({
                        'key': key,
                        'value1': value[0],
                        'value2': value[1]
                    })
            else:
                results.append({
                    'key': None,
                    'value1': None,
                    'value2': f"Ничего не найдено для запроса: {search_value}"
                })

        return JsonResponse({'results': results})

    return JsonResponse({'error': 'Метод не разрешен'}, status=405)


@csrf_exempt
def search2(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        search_values = data.get('search_values', [])

        results2 = []
        for search_value2 in search_values:
            key_result2 = dict2.get(search_value2) or dict2.get(search_value2.upper()) or dict2.get(
                search_value2.lower())

            value_results2 = [
                (key, value) for key, value in dict2.items()
                if search_value2.lower() == value[1].lower()
            ]

            if key_result2:
                results2.append({
                    'key': search_value2,
                    'value1': key_result2[0],
                    'value2': key_result2[1]
                })
            elif value_results2:
                for key, value in value_results2:
                    results2.append({
                        'key': key,
                        'value1': value[0],
                        'value2': value[1]
                    })
            else:
                results2.append({
                    'key': None,
                    'value1': None,
                    'value2': f"Ничего не найдено для запроса: {search_value2}"
                })

        return JsonResponse({'results': results2})

    return JsonResponse({'error': 'Метод не разрешен'}, status=405)

#VALUE
#def get_articles
