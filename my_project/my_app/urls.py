from . import views
from django.urls import path

app_name = 'my_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),


]