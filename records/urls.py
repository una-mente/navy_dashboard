from django.urls import path
from . import views

urlpatterns = [
    path(r'<str:model>/<str:selection_group>/<str:data_format>/', views.my_incidents, name="my_incidents"),
]
