from django.urls import path
from converter import views

urlpatterns = [
    path("students/",views.details_list),
    path("students/<int:pk>/",views.detail_individual),
    path("fileupload/",views.addfile),
]
