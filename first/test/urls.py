from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="test-index"),
    # path("all", views.all, name="test-all"),
]
