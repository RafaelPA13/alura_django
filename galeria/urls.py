from django.urls import path
from galeria.views import imagem, index

urlpatterns = [
    path("", index),
    path("imagem/<int:foto_id>/", imagem, name="imagem"),
]