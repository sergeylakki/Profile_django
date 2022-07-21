from django.urls import path

from . import views

urlpatterns = [
    path('user/<int:pk>', views.UserDetailView.as_view(), name='index'),
]