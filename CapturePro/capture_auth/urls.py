from django.urls import path
from capture_auth import views

urlpatterns = [
path('',views.employeeDashbord,name="userCemployeedashbordrud"),
path('signin/', views.signIn, name="signin"), 
path('signup/',views.signUp,name="signup"),
path('adminDashboard/',views.adminDashboard,name="adminDashboard"),
path('userCrud/',views.userCrud,name="userCrud"),
]