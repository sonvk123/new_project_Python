from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="employee-index"),
    path("all", views.all, name="employee-all"),
    path("all/<str:name>", views.hello, name="employee-hello"),
    path("getProduct", views.getProduct, name="employee-getProduct"),
    path("postProduct", views.postProduct, name="employee-postProduct"),
    # path("getProduct/", views.postProduct, name="employee-postProduct"),
]
