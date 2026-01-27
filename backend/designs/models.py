from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class DesignImage(models.Model):
    """
    Stores every uploaded design image.
    Used as a global reference pool for future plagiarism checks.
    """

    image = models.ImageField(upload_to="designs/")
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DesignImage {self.id} by {self.uploaded_by}"
