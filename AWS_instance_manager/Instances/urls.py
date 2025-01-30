from django.urls import path
from . import views
from .views import Signup

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', views.Signin, name='login'),
    path('logout/', views.logout, name='logout'),
]