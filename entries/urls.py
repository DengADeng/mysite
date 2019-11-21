from django.urls import path
from . import views
app_name = 'entries'
urlpatterns = [
    path('', views.HomeView.as_view(), name='blog-home'),
    path('entry/<int:pk>/', views.EntryView, name='entry_detail'),
    path('create_entry/', views.CreateEntry.as_view(success_url='/'), name='create_entry')
]
