from . import views
from django.urls import path

app_name = 'my_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),


]