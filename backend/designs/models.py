from django.conf import settings
from django.db import models


class DesignImage(models.Model):
    """
    Stores every uploaded design image.
    Used as a global reference pool for future plagiarism checks.
    """

    image = models.ImageField(upload_to="designs/")
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="design_images"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DesignImage {self.id} by {self.uploaded_by}"
