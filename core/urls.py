from django.urls import path
from .views import Inicio,Lista,Crear,ModificarColab,EliminarColab

urlpatterns =[
    path ('', Inicio, name="Inicio"),
    path ('Lista', Lista, name="Lista"),
    path ('Crear', Crear, name="Crear"),
    path ('ModificarColab/<id>', ModificarColab, name="ModificarColab"),
    path ('EliminarColab/<id>', EliminarColab, name="EliminarColab")


]




