from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from .api import *


urlpatterns = [
    path('', views.home, name=''),
    path('register', views.register, name='register' ),
    path('my-login', views.my_login, name='my-login'),
    path('user-logout',views.user_logout, name='user-logout'),

    #--CRUD
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-record', views.create_record, name='create-record'),
    path('update-record/<int:pk>', views.update_record, name='update-record'),
    path('view-record/<int:pk>',views.view_record, name='view-record'),
    path('delete-record/<int:pk>', views.delete_record, name='delete-record'),

    # ---API
    path('api/register', api_register, name='api-register'),
    path('api/login', api_login, name='api-register'),
    path('api/logout', api_logout, name='api-register'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

