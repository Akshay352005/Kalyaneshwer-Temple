from django.contrib import admin

# pyrefly: ignore [missing-import]
from modeltranslation.admin import TranslationAdmin
from .models import (
    Service, GalleryItem, SiteSetting, Highlight,
    HomePageContent, AboutPageContent, Event, EventImage, EventVideo,
    TeamMember, SocialMediaLink
)


# ─────────────────────────────────────────────
#  SOCIAL MEDIA
# ─────────────────────────────────────────────
@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('platform',)


# ─────────────────────────────────────────────
#  HOMEPAGE
# ─────────────────────────────────────────────
@admin.register(HomePageContent)
class HomePageContentAdmin(TranslationAdmin):
    fieldsets = (
        ('🖼️  Hero Banner', {
            'description': 'This is the large image at the top of the home page.',
            'fields': ('hero_image', 'hero_title', 'hero_subtitle'),
        }),
        ('🔘  Buttons', {
            'description': 'Configure the two buttons shown in the hero section.',
            'fields': (
                ('cta_button_text', 'cta_button_link'),
                ('secondary_button_text', 'secondary_button_link'),
            ),
        }),
        ('💛  Donation Section', {
            'fields': ('support_title', 'support_text'),
        }),
    )
    def has_add_permission(self, request):
        return not HomePageContent.objects.exists()


# ─────────────────────────────────────────────
#  ABOUT PAGE
# ─────────────────────────────────────────────
@admin.register(AboutPageContent)
class AboutPageContentAdmin(TranslationAdmin):
    fieldsets = (
        ('📖  About Page', {
            'description': 'Content shown on the About Us page.',
            'fields': ('title', 'content', 'image'),
        }),
    )
    def has_add_permission(self, request):
        return not AboutPageContent.objects.exists()


# ─────────────────────────────────────────────
#  HIGHLIGHTS
# ─────────────────────────────────────────────
@admin.register(Highlight)
class HighlightAdmin(TranslationAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    fieldsets = (
        ('✨  Highlight Card', {
            'fields': ('title', 'description', 'order'),
        }),
        ('🎨  Image or Icon', {
            'description': 'Upload a photo OR pick an icon. If you upload a photo it will be used.',
            'fields': ('image', 'icon'),
        }),
    )


# ─────────────────────────────────────────────
#  SERVICES
# ─────────────────────────────────────────────
@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    fieldsets = (
        ('🛕  Service Details', {
            'fields': ('title', 'description', 'image'),
        }),
    )


# ─────────────────────────────────────────────
#  EVENTS
# ─────────────────────────────────────────────
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1
    verbose_name = "📸 Event Photo"
    verbose_name_plural = "📸 Event Photos (Gallery)"

class EventVideoInline(admin.TabularInline):
    model = EventVideo
    extra = 1
    verbose_name = "🎬 Additional Video"
    verbose_name_plural = "🎬 Additional Videos"

@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ('title', 'event_date', 'location')
    search_fields = ('title', 'location')
    list_filter = ('event_date',)
    inlines = [EventImageInline, EventVideoInline]
    fieldsets = (
        ('📅  Event Information', {
            'fields': ('title', 'event_date', 'location', 'description'),
        }),
        ('📸  Media', {
            'description': 'Main photo and promotional video. Add more photos/videos in the sections below.',
            'fields': ('image', 'video_url'),
        }),
    )


# ─────────────────────────────────────────────
#  GALLERY
# ─────────────────────────────────────────────
@admin.register(GalleryItem)
class GalleryItemAdmin(TranslationAdmin):
    list_display = ('title', 'created_at', 'video_url')
    search_fields = ('title',)
    fieldsets = (
        ('🖼️  Gallery Item', {
            'fields': ('title', 'image', 'video_url'),
        }),
    )


# ─────────────────────────────────────────────
#  TRUST / TEAM
# ─────────────────────────────────────────────
@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'role')
    fieldsets = (
        ('👤  Member Details', {
            'fields': ('name', 'role', 'description', 'order'),
        }),
        ('🎨  Photo or Icon', {
            'description': 'Upload a photo OR enter a FontAwesome icon class. Photo takes priority.',
            'fields': ('image', 'icon'),
        }),
    )


# ─────────────────────────────────────────────
#  SITE SETTINGS
# ─────────────────────────────────────────────
@admin.register(SiteSetting)
class SiteSettingAdmin(TranslationAdmin):
    list_display = ('key', 'value')
    search_fields = ('key', 'value')
