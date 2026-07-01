from django.core.management.base import BaseCommand
from core.models import HomePageContent, AboutPageContent

class Command(BaseCommand):
    help = 'Populates initial translations for HomePageContent and AboutPageContent models.'

    def handle(self, *args, **options):
        # 1. HomePageContent
        hp, _ = HomePageContent.objects.get_or_create(id=1)
        
        # Hindi
        hp.hero_title_hi = "कल्याणेश्वर मंदिर में आपका स्वागत है"
        hp.hero_subtitle_hi = "शांति, प्रार्थना और आध्यात्मिक जागरण के लिए एक दिव्य अभयारण्य।"
        hp.cta_button_text_hi = "पूजा बुक करें"
        hp.secondary_button_text_hi = "और जानें"
        hp.support_title_hi = "हमारे मिशन का समर्थन करें"
        hp.support_text_hi = "आपका उदार दान हमें मंदिर को बनाए रखने, दैनिक अनुष्ठान करने और हमारी धर्मार्थ गतिविधियों में मदद करता है।"
        
        # Kannada
        hp.hero_title_kn = "ಕಲ್ಯಾಣೇಶ್ವರ ದೇವಸ್ಥಾನಕ್ಕೆ ಸ್ವಾಗತ"
        hp.hero_subtitle_kn = "ಶಾಂತಿ, ಪ್ರಾರ್ಥನೆ ಮತ್ತು ಆಧ್ಯಾತ್ಮಿಕ ಜಾಗೃತಿಗಾಗಿ ಒಂದು ದೈವಿಕ ಅಭಯಾರಣ್ಯ."
        hp.cta_button_text_kn = "ಪೂಜೆಯನ್ನು ಕಾಯ್ದಿರಿಸಿ"
        hp.secondary_button_text_kn = "ಇನ್ನಷ್ಟು ತಿಳಿಯಿರಿ"
        hp.support_title_kn = "ನಮ್ಮ ಉದ್ದೇಶವನ್ನು ಬೆಂಬಲಿಸಿ"
        hp.support_text_kn = "ನಿಮ್ಮ ಉದಾರ ದೇಣಿಗೆಯು ದೇವಾಲಯವನ್ನು ನಿರ್ವಹಿಸಲು, ದೈನಂದಿನ ಆಚರಣೆಗಳನ್ನು ಮಾಡಲು ಮತ್ತು ನಮ್ಮ ದತ್ತಿ ಚಟುವಟಿಕೆಗಳನ್ನು ಬೆಂಬಲಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ."
        
        # Ensure EN is also set correctly from defaults if empty
        if not hp.hero_title_en: hp.hero_title_en = hp.hero_title
        if not hp.hero_subtitle_en: hp.hero_subtitle_en = hp.hero_subtitle
        if not hp.cta_button_text_en: hp.cta_button_text_en = hp.cta_button_text
        if not hp.secondary_button_text_en: hp.secondary_button_text_en = hp.secondary_button_text
        if not hp.support_title_en: hp.support_title_en = hp.support_title
        if not hp.support_text_en: hp.support_text_en = hp.support_text

        hp.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated HomePageContent translations.'))

        # 2. AboutPageContent
        ap, _ = AboutPageContent.objects.get_or_create(id=1)
        
        # Hindi
        ap.title_hi = "हमारे बारे में"
        ap.content_hi = "हम सभी भक्तों के लिए एक शांतिपूर्ण और दिव्य वातावरण प्रदान करने के लिए समर्पित हैं।"
        
        # Kannada
        ap.title_kn = "ನಮ್ಮ ಬಗ್ಗೆ"
        ap.content_kn = "ಎಲ್ಲಾ ಭಕ್ತರಿಗೆ ಶಾಂತಿಯುತ ಮತ್ತು ದೈವಿಕ ವಾತಾವರಣವನ್ನು ಒದಗಿಸಲು ನಾವು ಸಮರ್ಪಿತರಾಗಿದ್ದೇವೆ।"
        
        # English
        if not ap.title_en: ap.title_en = ap.title
        if not ap.content_en: ap.content_en = ap.content
        
        ap.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated AboutPageContent translations.'))
