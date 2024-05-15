from django.urls import path
from . import views
urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("lectures/<int:id>/", views.course_lectures, name="lectures"),
]