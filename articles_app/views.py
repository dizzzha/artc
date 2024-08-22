from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .output_dict import dictionary
from .output_dict2 import dictionary


def index(request):
    return render(request, 'index.html')


def get_value_for_key(key):
    return dictionary.get(key, "Значение не найдено")


def get_value(request):
    if request.method == 'POST':
        keys = json.loads(request.POST.get('keys'))
        values = [get_value_for_key(key) for key in keys]
        return JsonResponse({'values': values})


@csrf_exempt
def get_keys(request):
    current_dict = request.session.get('current_dict', 'floor_1_dict')
    if current_dict == 'floor_1_dict':
        from .output_dict import dictionary
    else:
        from .output_dict2 import dictionary
    keys = list(dictionary.keys())
    return JsonResponse({'keys': keys})


@csrf_exempt
def get_values(request):
    current_dict = request.session.get('current_dict', 'floor_1_dict')
    if current_dict == 'floor_1_dict':
        from .output_dict import dictionary
    else:
        from .output_dict2 import dictionary
    values = [value[1] for value in dictionary.values()]
    return JsonResponse({'values': values})


@csrf_exempt
def search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        search_values = data.get('search_values', [])

        # Выбор словаря в зависимости от выбранного этажа
        current_dict = request.session.get('current_dict', 'floor_1_dict')
        if current_dict == 'floor_1_dict':
            from .output_dict import dictionary
        else:
            from .output_dict2 import dictionary

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
                    'value2': key_result[1],
                    'image_query': key_result[1]  # Используем второй элемент как запрос для изображения
                })
            elif value_results:
                for key, value in value_results:
                    results.append({
                        'key': key,
                        'value1': value[0],
                        'value2': value[1],
                        'image_query': value[1]  # Используем второй элемент как запрос для изображения
                    })
            else:
                results.append({
                    'key': None,
                    'value1': None,
                    'value2': f"Ничего не найдено для запроса: {search_value}",
                    'image_query': None
                })

        return JsonResponse({'results': results})

    return JsonResponse({'error': 'Метод не разрешен'}, status=405)


@csrf_exempt
def set_floor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        floor = data.get('floor')

        if floor == 1:
            from .output_dict import dictionary as floor_1_dict
            request.session['current_dict'] = 'floor_1_dict'
        elif floor == 2:
            from .output_dict2 import dictionary as floor_2_dict
            request.session['current_dict'] = 'floor_2_dict'
        else:
            return JsonResponse({'error': 'Invalid floor'}, status=400)

        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request method'}, status=405)

#VALUE
#def get_articles
