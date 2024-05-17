from . import views
from django.urls import path

app_name = 'my_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:customer_id>/', views.update_customer, name='update_customer'),
    path('search_customer/', views.search_customer, name='search_customer'),


]