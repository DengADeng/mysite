from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('comment/<int:entry_pk>', views.comment, name='comment'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout')
]
