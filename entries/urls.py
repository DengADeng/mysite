from django.urls import path
from . import views
app_name = 'entries'
urlpatterns = [
    path('', views.HomeView.as_view(), name='blog-home'),
    path('entry/<int:pk>/', views.EntryView, name='entry_detail'),
    path('category/', views.CategoryView, name='category')
]
