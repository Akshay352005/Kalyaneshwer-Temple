from modeltranslation.translator import register, TranslationOptions
from .models import Service, GalleryItem, SiteSetting, Highlight, HomePageContent, AboutPageContent, Event, TeamMember

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(GalleryItem)
class GalleryItemTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(SiteSetting)
class SiteSettingTranslationOptions(TranslationOptions):
    fields = ('value',)

@register(Highlight)
class HighlightTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(HomePageContent)
class HomePageContentTranslationOptions(TranslationOptions):
    fields = ('hero_title', 'hero_subtitle', 'cta_button_text', 'secondary_button_text', 'support_title', 'support_text')

@register(AboutPageContent)
class AboutPageContentTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'location')

@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'role', 'description')
