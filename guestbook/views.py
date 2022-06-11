from rest_framework import permissions

from assignment.generics import ExtendedRetrieveUpdateDestroyAPIView, ExtendedListCreateAPIView, \
    StandardResultsSetPagination
from guestbook.models import GuestBook
from guestbook.serializers import GuestBookRetrieveUpdateDestroySerializer, GuestBookListCreateSerializer


class GuestBookRetrieveUpdateDestroyAPIView(ExtendedRetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = GuestBook.objects.all()
    serializer_class = GuestBookRetrieveUpdateDestroySerializer
    lookup_field = 'id'

    def get_queryset(self):
        return GuestBook.objects.filter(created_by=self.request.user)


class GuestBookListCreateAPIView(ExtendedListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = StandardResultsSetPagination
    serializer_class = GuestBookListCreateSerializer
    queryset = GuestBook.objects.all()
    filterset_fields = ['name']
