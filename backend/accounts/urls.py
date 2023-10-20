from django.urls import path

from .views import *

urlpatterns = [
    #Accounts URLs
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    #Profile URLs
    path('api/profile-update/<int:profile_id>/', ProfileUpdate.as_view(), name='profile-update'),
    path('api/profile-detail/<int:profile_user_id>/', ProfileDetail.as_view(), name='profile-detail'),
    #Follow URLs
    path('api/follow/profile/<int:profile_user_id>/', follow_profile, name='follow-profile')
]