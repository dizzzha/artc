from django.urls import path
from articles_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_value/', views.get_value, name='get_value'),
    path('get_keys/', views.get_keys, name='get_keys'),
    path('get_values/', views.get_values, name='get_values'),
    path('search/', views.search, name='search'),
]
