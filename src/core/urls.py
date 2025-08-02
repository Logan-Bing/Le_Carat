from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("success/<int:customer_id>/", views.success_view, name="success"),
]
