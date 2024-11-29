from django.urls import path
from .views import LoginView, activate_user_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('activate/<uuid:id>/', activate_user_view, name='activate-user'),
]
