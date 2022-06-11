from django.conf.urls import url

from guestbook.views import GuestBookRetrieveUpdateDestroyAPIView, GuestBookListCreateAPIView

urlpatterns = [
    url(r'^', GuestBookListCreateAPIView.as_view(),
        name='guestbook_list_create_api_view'),
    url(r'^(?P<id>[\w-]+)$', GuestBookRetrieveUpdateDestroyAPIView.as_view(),
        name='guestbook_retrieve_update_destroy_api_view'),
]
