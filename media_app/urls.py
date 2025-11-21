from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_list, name='media_list'),
    path('edit/<int:media_id>/', views.edit_media, name='edit_media'),
    path('delete/<int:media_id>/', views.delete_media, name='delete_media'),
]
