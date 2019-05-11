from django.urls import path

from .views import SchoolView

urlpatterns = [
    path('schools/', SchoolView.as_view(), name='school'),
]