from django.contrib import admin

from .models import (
    ContactInquiry,
    Event,
    LeadershipProfile,
    MediaGalleryItem,
    NewsUpdate,
    Partner,
    Resource,
)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "location", "is_published")
    list_filter = ("is_published", "event_date")
    search_fields = ("title", "summary", "details", "location")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(NewsUpdate)
class NewsUpdateAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at", "is_published")
    list_filter = ("is_published", "published_at")
    search_fields = ("title", "summary", "body", "author")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(LeadershipProfile)
class LeadershipProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role_title", "display_order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("full_name", "role_title", "bio")
    ordering = ("display_order", "full_name")


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "display_order", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name", "category", "description")
    ordering = ("display_order", "name")


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "created_at")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "category", "description")


@admin.register(MediaGalleryItem)
class MediaGalleryItemAdmin(admin.ModelAdmin):
    list_display = ("title", "event_name", "created_at")
    search_fields = ("title", "caption", "event_name")


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "inquiry_type", "created_at")
    list_filter = ("inquiry_type", "created_at")
    search_fields = ("full_name", "email", "organization", "message")
    readonly_fields = ("created_at",)
