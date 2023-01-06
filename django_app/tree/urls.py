from django.urls import path
from .views import show_menu

urlpatterns = [
    path('menu/<int:pk>/', show_menu, name='menu'),
]