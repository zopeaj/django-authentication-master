from django.urls import path
from account.views import register, login, logout, account_home

urlpatterns = [
    path('', account_home, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('register', register, name='register')
]
