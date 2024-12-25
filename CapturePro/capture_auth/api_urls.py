#region imports
from django.urls import path
from .api_views import SignUpView, SignInView, UserListView, UserDetailView, CompanyProfileViewSet, EmployeeProfileViewSet,EmailVerificationView
#endregion

#region API urls
urlpatterns = [
    #region authorization URL
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('verify-email/<uidb64>/<token>/', EmailVerificationView.as_view(), name='verify-email'),
    #endregion

    #region user management URL
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    #endregion

    #region company and employee profiles URLs
    path('company-profiles/', CompanyProfileViewSet.as_view(), name='company-profile-list'),
    path('employee-profiles/', EmployeeProfileViewSet.as_view(), name='employee-profile-list'),
    #endregion

]
#endregion