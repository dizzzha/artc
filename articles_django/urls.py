from django.urls import path
from articles_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second_floor/', views.second_floor, name='second_floor'),
    path('get_value/', views.get_value, name='get_value'),
    path('get_keys/', views.get_keys, name='get_keys'),
    path('get_keys2/', views.get_keys2, name='get_keys2'),
    path('get_values/', views.get_values, name='get_values'),
    path('get_values2/', views.get_values2, name='get_values2'),
    path('search/', views.search, name='search'),
    path('search2/', views.search2, name='search'),
]
