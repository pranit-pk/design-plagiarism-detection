from django.db import models
from django.conf import settings
from designs.models import DesignImage


class Report(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reports"
    )

    image_1 = models.ForeignKey(
        DesignImage,
        on_delete=models.CASCADE,
        related_name="reports_as_image_1"
    )

    image_2 = models.ForeignKey(
        DesignImage,
        on_delete=models.CASCADE,
        related_name="reports_as_image_2"
    )

    scores = models.JSONField()
    final_score = models.FloatField()
    verdict = models.CharField(max_length=100)
    explanation = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report {self.id} | Score {self.final_score}"
