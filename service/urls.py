from django.urls import path
from . import views

app_name= "service"
urlpatterns = [
    path("", views.Index.as_view, name="Index"),
]
