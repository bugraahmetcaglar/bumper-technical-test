from django.conf.urls import url
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserLoginAPIView, UserRegistrationAPIView, UserLogoutAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    url(r'^user/detail/(?P<id>[\w-]+)$', UserDetailAPIView.as_view(), name='user_detail_api'),
    url(r'^user/login$', UserLoginAPIView.as_view(), name="user_login_api"),
    url(r'^user/list$', UserListAPIView.as_view(), name="user_list_api"),
    url(r'^user/login/refresh$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^user/register$', UserRegistrationAPIView.as_view(), name='user_create_api'),
    url(r'^user/logout$', UserLogoutAPIView.as_view(), name='user_logout_api'),
]
