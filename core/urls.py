from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'services-list', views.ServiceViewSet, basename='service')
router.register(r'gallery-list', views.GalleryViewSet, basename='gallery')
router.register(r'events-list', views.EventViewSet, basename='event')
router.register(r'team-list', views.TeamMemberViewSet, basename='teammember')
router.register(r'social-links', views.SocialMediaLinkViewSet, basename='socialmedialink')

urlpatterns = [
    path('home/', views.HomePageAPIView.as_view(), name='api_home'),
    path('about/', views.AboutPageAPIView.as_view(), name='api_about'),
    path('services/', views.ServiceViewSet.as_view({'get': 'list'}), name='api_services'),
    path('events/', views.EventsAPIView.as_view(), name='api_events'),
    path('site-settings/', views.SiteSettingsAPIView.as_view(), name='api_site_settings'),
    path('', include(router.urls)),
]
