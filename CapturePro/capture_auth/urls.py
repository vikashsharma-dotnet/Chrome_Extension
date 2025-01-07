from django.urls import path
from capture_auth import views

urlpatterns = [
path('', views.signIn, name="signIn"), 
path('home/',views.home,name="home"),
path('signup/',views.signUp,name="signup"),
path('adminDashboard/',views.adminDashboard,name="adminDashboard"),
path('userCrud/',views.userCrud,name="userCrud"),
path('subscription/',views.subscription,name="subscription"),
]