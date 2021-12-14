from django.contrib import admin

# Register your models here.
from .models import news


class newsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("News", {"fields": ["title", "link", "published"]}),
        ("DB Dates", {"fields": ["created_at, updated_at"]}),
        ("Source", {"fields": ["source"]}),
    ]
admin.site.register(news ,newsAdmin)