from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from redact_radar.models import Newspaper, Topic, Redactor

admin.site.unregister(Group)


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("title", "get_topics", "published_date", )
    search_fields = ("title", )
    ordering = ("-published_date",)

    def get_topics(self, obj) -> str:
        return ", ".join([topic.name for topic in obj.dish_type.all()])
    get_topics.short_description = "Topics"


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (
        ("User Information", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("User Information", {"fields": ("years_of_experience",)}),
    )
    search_fields = ("username", )
    ordering = ("username", )


admin.site.register(Topic)
