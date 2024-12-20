from django.urls import path
from capture_auth import views

urlpatterns = [
path('',views.signIn,name="signin"),
path('signup/',views.signUp,name="signup"),

]