from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('vacancy/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('vacancy/new/', views.vacancy_create, name='vacancy_create'),
    path('vacancy/<int:pk>/edit/', views.vacancy_update, name='vacancy_update'),
    path('vacancy/<int:pk>/delete/', views.vacancy_delete, name='vacancy_delete'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/', views.job_list, name='job_list'),
]