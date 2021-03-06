from django.contrib import admin

from .models import Event, EventMember,NewComment

# Register your models here.

admin.site.register(EventMember)
admin.site.register(NewComment)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_date", "slug", "image"]
    list_display_links = ["title", "created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]

    class Meta:
        model = Event
