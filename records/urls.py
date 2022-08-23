from django.urls import path
from . import views

urlpatterns = [
    path(r'<str:model>/<str:selection_group>/', views.my_incidents, name="my_incidents"),
]
