from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="api_register"),
    path("token/", TokenObtainPairView.as_view(), name="obtain_jwt"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_jwt"),
    path('oauth2/github/', views.GithubLoginAPIView.as_view(), name="obtain_oauth_login_url"),
    path('oauth2/github/authenticate/', views.GithubAuthView.as_view(), name="github_authenticate_view"),
    path("profile/upload/", views.UpdateProfileView.as_view(), name="api_upload_profile_info"),
    path("profile/", views.ProfileView.as_view(), name="api_get_profile"),
    path("profile/glimps/<int:pk>", views.ProfileGlimpsAPIView.as_view(), name="api_get_profile_glimps"),
    path("bookmarks/add/", views.SavePostView.as_view(), name="api_save_post"),
    path("bookmarks/delete/", views.SavePostView.as_view(), name="api_remove_saved_post"),
    path("followers/follow/", views.FollowAPIView.as_view(), name="api_follow_user"),
    path("followers/unfollow/", views.FollowAPIView.as_view(), name="api_unfollow_user"),
    path("list/", views.UserListAPIView.as_view(), name="api_users_list"),
]
