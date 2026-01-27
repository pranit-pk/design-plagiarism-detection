from django.contrib import admin
from .models import DesignImage

@admin.register(DesignImage)
class DesignImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "uploaded_by", "created_at")
