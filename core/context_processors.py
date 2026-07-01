from django.utils.translation import gettext_lazy as _
from .models import SiteSetting, SocialMediaLink

def site_settings(request):
    settings = SiteSetting.objects.all()
    settings_dict = {s.key: s.value for s in settings}
    
    # Provide translated defaults if keys are missing
    if 'address' not in settings_dict:
        settings_dict['address'] = _("Temple Road, Holy City")
    if 'phone' not in settings_dict:
        settings_dict['phone'] = "+91 98765 43210"
    if 'email' not in settings_dict:
        settings_dict['email'] = "info@kalyaneshwari.org"
        
    social_links = SocialMediaLink.objects.filter(is_active=True)
    return {
        'site_settings': settings_dict,
        'social_links': social_links,
    }
