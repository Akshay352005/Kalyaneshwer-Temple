from django.shortcuts import render
from .models import Service, GalleryItem, HomePageContent, AboutPageContent, Highlight

def home(request):
    home_content = HomePageContent.load()
    highlights = Highlight.objects.all()
    services = Service.objects.all()[:3]
    gallery = GalleryItem.objects.all()[:3]
    
    return render(request, 'core/home.html', {
        'home_content': home_content,
        'highlights': highlights,
        'services': services,
        'gallery': gallery
    })

def about(request):
    about_content = AboutPageContent.load()
    from .models import TeamMember
    team_members = TeamMember.objects.all()
    return render(request, 'core/about.html', {'about_content': about_content, 'team_members': team_members})

def donations(request):
    return render(request, 'core/donations.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})

def events(request):
    from .models import Event
    from django.utils import timezone
    now = timezone.now()
    upcoming_events = Event.objects.filter(event_date__gte=now).order_by('event_date')
    past_events = Event.objects.filter(event_date__lt=now).order_by('-event_date')
    return render(request, 'core/events.html', {'upcoming_events': upcoming_events, 'past_events': past_events})
