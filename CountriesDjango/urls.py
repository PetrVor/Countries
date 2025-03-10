
from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('countries-list', views.countries),
    path('country/<str:country_name>', views.get_country),
    path('sorted-list/<str:check>', views.starts_letter),
    path('languages-list', views.languages),
    path('language/<str:lang>', views.get_lang),
]
