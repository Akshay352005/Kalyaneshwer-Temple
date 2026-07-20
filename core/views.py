from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.utils import timezone

from .models import (
    SocialMediaLink,
    Service,
    GalleryItem,
    SiteSetting,
    Highlight,
    HomePageContent,
    AboutPageContent,
    Event,
    TeamMember
)
from .serializers import (
    SocialMediaLinkSerializer,
    ServiceSerializer,
    GalleryItemSerializer,
    SiteSettingSerializer,
    HighlightSerializer,
    HomePageContentSerializer,
    AboutPageContentSerializer,
    EventSerializer,
    TeamMemberSerializer
)


class HomePageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        home_content = HomePageContent.load()
        highlights = Highlight.objects.all()
        services = Service.objects.all()[:3]
        gallery = GalleryItem.objects.all()[:3]

        return Response({
            'home_content': HomePageContentSerializer(home_content, context={'request': request}).data,
            'highlights': HighlightSerializer(highlights, many=True, context={'request': request}).data,
            'services': ServiceSerializer(services, many=True, context={'request': request}).data,
            'gallery': GalleryItemSerializer(gallery, many=True, context={'request': request}).data,
        })


class AboutPageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        about_content = AboutPageContent.load()
        team_members = TeamMember.objects.all()

        return Response({
            'about_content': AboutPageContentSerializer(about_content, context={'request': request}).data,
            'team_members': TeamMemberSerializer(team_members, many=True, context={'request': request}).data,
        })


class EventsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        now = timezone.now()
        upcoming = Event.objects.filter(event_date__gte=now).order_by('event_date')
        past = Event.objects.filter(event_date__lt=now).order_by('-event_date')

        return Response({
            'upcoming_events': EventSerializer(upcoming, many=True, context={'request': request}).data,
            'past_events': EventSerializer(past, many=True, context={'request': request}).data,
        })


class SiteSettingsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        settings_qs = SiteSetting.objects.all()
        settings_dict = {s.key: s.value for s in settings_qs}
        
        # Defaults if missing
        if 'address' not in settings_dict:
            settings_dict['address'] = "Temple Road, Holy City"
        if 'phone' not in settings_dict:
            settings_dict['phone'] = "+91 98765 43210"
        if 'email' not in settings_dict:
            settings_dict['email'] = "info@kalyaneshwari.org"

        social_links = SocialMediaLink.objects.filter(is_active=True)

        return Response({
            'site_settings': settings_dict,
            'social_links': SocialMediaLinkSerializer(social_links, many=True, context={'request': request}).data
        })


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class GalleryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class SocialMediaLinkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialMediaLink.objects.filter(is_active=True)
    serializer_class = SocialMediaLinkSerializer
