from django.contrib import admin
from .models import Templates, Content

@admin.register(Templates)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ("id", "template_name", "created_at", "updated_at")
    search_fields = ("template_name",)
    ordering = ("id",)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "template", "section_type", "created_at", "updated_at")
    search_fields = ("template__template_name", "section_type")
    ordering = ("id",)
