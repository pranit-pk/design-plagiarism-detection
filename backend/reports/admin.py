from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "verdict", "final_score", "created_at")
    list_filter = ("verdict", "created_at")
    search_fields = ("user__username",)
