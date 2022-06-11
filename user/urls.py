from django.conf.urls import url
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserLoginAPIView, UserRegistrationAPIView, UserLogoutAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    url(r'^user/login$', UserLoginAPIView.as_view(), name="user_login"),
    url(r'^user/list$', UserListAPIView.as_view(), name="user_login"),
    url(r'^user/login/refresh$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^user/register$', UserRegistrationAPIView.as_view()),
    url(r'^user/logout$', UserLogoutAPIView.as_view()),
    url(r'^user/detail/(?P<id>[\w-]+)$', UserDetailAPIView.as_view()),
]
