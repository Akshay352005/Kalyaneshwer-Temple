from rest_framework import serializers
from .models import (
    SocialMediaLink,
    Service,
    GalleryItem,
    SiteSetting,
    Highlight,
    HomePageContent,
    AboutPageContent,
    Event,
    EventImage,
    EventVideo,
    TeamMember
)

class SocialMediaLinkSerializer(serializers.ModelSerializer):
    icon_class = serializers.ReadOnlyField()

    class Meta:
        model = SocialMediaLink
        fields = ['id', 'platform', 'url', 'order', 'is_active', 'icon_class']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'image', 'created_at']


class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = ['id', 'title', 'image', 'video_url', 'created_at']


class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = ['id', 'key', 'value']


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = ['id', 'title', 'description', 'icon', 'image', 'order']


class HomePageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageContent
        fields = [
            'hero_title',
            'hero_subtitle',
            'hero_image',
            'cta_button_text',
            'cta_button_link',
            'secondary_button_text',
            'secondary_button_link',
            'support_title',
            'support_text'
        ]


class AboutPageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPageContent
        fields = ['title', 'content', 'image']


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ['id', 'image', 'caption']


class EventVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVideo
        fields = ['id', 'video_url', 'title']


class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    videos = EventVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'description',
            'image',
            'video_url',
            'event_date',
            'location',
            'created_at',
            'images',
            'videos'
        ]


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'role', 'description', 'image', 'icon', 'order']
