from django.urls import path
from . import views  # o "." indica a pasta atual. importa a view porque é o que vai aparecer na tela

urlpatterns = [
    path('', views.index),
]