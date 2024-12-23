from django.urls import path
from .api_views import SignUpView, SignInView, UserListView, UserDetailView, CompanyProfileViewSet, EmployeeProfileViewSet

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('company-profiles/', CompanyProfileViewSet.as_view(), name='company-profile-list'),
    path('employee-profiles/', EmployeeProfileViewSet.as_view(), name='employee-profile-list'),
]
