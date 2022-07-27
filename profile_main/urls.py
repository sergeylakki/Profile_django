from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user'),
    path('character/add/', views.CharacteristicsUserCreateView.as_view(), name='character-add'),
    path('character/<int:pk>/', views.CharacteristicsUserUpdateView.as_view(), name='character-update'),
    #path('character/<int:pk>/delete/', views.CharacteristicsUserDeleteView.as_view(), name='character-delete'),
    path('action/add/', views.ActionUserCreateView.as_view(), name='action-add'),
]