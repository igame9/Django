from django.urls import path
from . import views  # view из корня

urlpatterns = [
    path("", views.index, name="_index_"),
    path("next/", views.next, name="_next_"),
]
