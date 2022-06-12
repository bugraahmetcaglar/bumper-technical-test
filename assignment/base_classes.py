import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_by = models.ForeignKey('user.User', null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    updated_by = models.ForeignKey('user.User', null=True, blank=True, on_delete=models.SET_NULL, related_name="+")
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

