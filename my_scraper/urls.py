from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('form/', views.scrape_view, name='scrape_form'),
    path('result/', views.scrape_view_result, name='scrape_result')
]