from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('add/', views.record_create, name='add_record'),          # <-- 'add_record' here
    path('edit/<int:pk>/', views.record_update, name='edit_record'),
    path('delete/<int:pk>/', views.record_delete, name='record_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]