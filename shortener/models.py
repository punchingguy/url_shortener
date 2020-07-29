from django.conf import settings #for importing SHORTCODE_MAX,MIN values from settings
from django.db import models
#from django.urls import reverse
from django_hosts.resolvers import reverse


from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_http

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15) #the value of SHORTCODE_MAX from settings and if it not there then bydefault 15

# Create your models here.
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs
    
    def refresh_shortcodes(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            # print(q.id)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return new_codes




class KirrURL(models.Model):
    url         = models.CharField(max_length=220, validators=[validate_url, validate_http])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    update      = models.DateTimeField(auto_now=True)#everytime the model is saved  
    timestamp   = models.DateTimeField(auto_now_add=True)#When model was created
    active      = models.BooleanField(default=True)

    objects = KirrURLManager()
    #some_random = KirrURLManager() 

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL,self).save(*args, **kwargs)


    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path


    
