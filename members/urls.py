from django.urls import path
from . import views

urlpatterns = [
    path('login_user',views.login_user,name='login_user'),
    path('logout_user',views.login_user,name='logout_user'),
    path('signin_user',views.signin_user,name='signin_user')
]