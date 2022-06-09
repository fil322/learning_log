from django.urls import path
from . import views

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Вывод всех тем.
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<topic_id>\d+/', views.topic, name='topic'),
    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для добавления новой записи
    path('new_entry/<topic_id>\d+/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<entry_id>\d+/', views.edit_entry, name='edit_entry'),
]