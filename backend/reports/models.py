from django.conf import settings
from django.db import models


class Report(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reports"
    )

    image_1 = models.ImageField(upload_to="comparisons/")
    image_2 = models.ImageField(upload_to="comparisons/")

    scores = models.JSONField()
    final_score = models.FloatField()
    verdict = models.CharField(max_length=50)
    explanation = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report #{self.id} - {self.verdict}"
