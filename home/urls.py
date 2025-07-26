from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('detail/<str:item_type>/<int:item_id>/', views.detail, name='detail'),
    path('booking/<str:item_type>/<int:item_id>/', views.booking, name='booking'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('orders/', views.user_orders, name='orders'),
]
