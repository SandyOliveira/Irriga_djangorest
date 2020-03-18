from django.urls import path

from .views import UsuarioView


app_name = "usuarios"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('usuarios/', UsuarioView.as_view()),
    path('usuarios/<int:pk>', UsuarioView.as_view()),

]