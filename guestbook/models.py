from django.db import models

# Create your models here.
from assignment.base_classes import BaseModel


class GuestBook(BaseModel):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        db_table = 'guestbook'
