from django.db import models

SOCIAL_PLATFORM_CHOICES = [
    ('facebook', 'Facebook'),
    ('instagram', 'Instagram'),
    ('twitter', 'Twitter / X'),
    ('youtube', 'YouTube'),
    ('whatsapp', 'WhatsApp'),
    ('telegram', 'Telegram'),
]

ICON_MAP = {
    'facebook': 'fa-brands fa-facebook',
    'instagram': 'fa-brands fa-instagram',
    'twitter': 'fa-brands fa-x-twitter',
    'youtube': 'fa-brands fa-youtube',
    'whatsapp': 'fa-brands fa-whatsapp',
    'telegram': 'fa-brands fa-telegram',
}

class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=50, choices=SOCIAL_PLATFORM_CHOICES, unique=True)
    url = models.URLField(help_text="Full URL e.g. https://facebook.com/YourTemples")
    order = models.IntegerField(default=0, help_text="Display order (lower = shown first)")
    is_active = models.BooleanField(default=True, help_text="Uncheck to hide from website")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_platform_display()} – {self.url}"

    @property
    def icon_class(self):
        return ICON_MAP.get(self.platform, 'fa-solid fa-link')


class Service(models.Model):
    title = models.CharField(max_length=200, help_text="Name of the puja or service")
    description = models.TextField(blank=True, help_text="Description shown on the website")
    image = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Upload a photo for this service")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class GalleryItem(models.Model):
    title = models.CharField(max_length=200, blank=True, help_text="Optional caption")
    image = models.ImageField(upload_to='gallery/', blank=True, null=True, help_text="Upload an image for the gallery")
    video_url = models.URLField(blank=True, null=True, help_text="Optional YouTube or Vimeo video link")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Gallery Item {self.id}"

class SiteSetting(models.Model):
    key = models.CharField(max_length=100, unique=True, help_text="e.g., 'email', 'phone', 'address'")
    value = models.TextField(help_text="The value for this setting")

    def __str__(self):
        return f"{self.key}: {self.value[:30]}"

class Highlight(models.Model):
    title = models.CharField(max_length=200, help_text="Short title for this highlight")
    description = models.TextField(help_text="A brief description shown on the homepage")
    icon = models.CharField(max_length=50, default="fa-solid fa-bell", help_text="FontAwesome icon class (e.g., 'fa-solid fa-bell'). See fontawesome.com/icons")
    image = models.ImageField(upload_to='highlights/', blank=True, null=True, help_text="Upload an image instead of using an icon")
    order = models.IntegerField(default=0, help_text="Display order (lower = shown first)")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class HomePageContent(models.Model):
    hero_title = models.CharField(max_length=200, default="Welcome to Kalyaneshwer Temple", help_text="Main heading shown in the hero section")
    hero_subtitle = models.TextField(default="A divine sanctuary for peace, prayer, and spiritual awakening.", help_text="Subtitle text below the main heading")
    hero_image = models.ImageField(upload_to='home/', blank=True, null=True, help_text="Background image for the hero section")
    cta_button_text = models.CharField(max_length=50, default="Book a Puja", help_text="Text for the primary call-to-action button")
    cta_button_link = models.CharField(max_length=200, default="/services/", help_text="URL for the primary button (e.g. /services/)")
    secondary_button_text = models.CharField(max_length=50, default="Learn More", help_text="Text for the secondary button")
    secondary_button_link = models.CharField(max_length=200, default="/about/", help_text="URL for the secondary button")
    support_title = models.CharField(max_length=200, default="Support Our Mission", help_text="Heading for the donation section")
    support_text = models.TextField(default="Your generous donations help us maintain the temple, perform daily rituals, and support our charitable activities.", help_text="Body text for the donation section")

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Home Page Content"

class AboutPageContent(models.Model):
    title = models.CharField(max_length=200, default="About Us", help_text="Main heading on the About page")
    content = models.TextField(default="We are dedicated to providing a divine sanctuary...", help_text="About page body text. Use new lines to create paragraphs.")
    image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Photo shown alongside the about text")

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "About Page Content"

class Event(models.Model):
    title = models.CharField(max_length=200, help_text="Name of the event")
    description = models.TextField(help_text="Event details / description")
    image = models.ImageField(upload_to='events/', blank=True, null=True, help_text="Main event photo (shown as the card thumbnail)")
    video_url = models.URLField(blank=True, null=True, help_text="Main promotional video link (YouTube/Vimeo)")
    event_date = models.DateTimeField(help_text="Date and time of the event")
    location = models.CharField(max_length=200, blank=True, default="Kalyaneshwer Temple", help_text="Venue / location of the event")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_gallery/', help_text="Photo from this event")
    caption = models.CharField(max_length=200, blank=True, help_text="Optional caption for this photo")

class EventVideo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='videos')
    video_url = models.URLField(help_text="YouTube/Vimeo link")
    title = models.CharField(max_length=200, blank=True, help_text="Optional label for this video")

class TeamMember(models.Model):
    name = models.CharField(max_length=100, help_text="Full name of the trust member")
    role = models.CharField(max_length=100, help_text="Their role (e.g., 'President', 'Chief Priest')")
    description = models.TextField(blank=True, help_text="Brief description or bio")
    image = models.ImageField(upload_to='team/', blank=True, null=True, help_text="Profile photo")
    icon = models.CharField(max_length=50, default="fa-solid fa-user", help_text="Fallback FontAwesome icon if no photo (e.g., 'fa-solid fa-user-tie')")
    order = models.IntegerField(default=0, help_text="Display order")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
