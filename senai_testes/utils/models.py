from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, null=True, blank=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, null=True, blank=True
    )

    class Meta:
        abstract = True
