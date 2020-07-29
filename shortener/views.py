from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View

from analytics.models import ClickEvent
from .forms import SubmitUrlForm
from .models import KirrURL
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Kirr.co",
            "form": the_form
        }
       
        return render(request, "shortener/home.html", context)
    
    def post(self, request, *args, **kwargs):
        the_form = SubmitUrlForm(request.POST)
        context = {
            "title": "Kirr.co",
            "form": the_form
        }
        template =  "shortener/home.html"

        if the_form.is_valid():
            new_url = the_form.cleaned_data['url']
            # print(new_url)
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created: 
               template = "shortener/success.html"
            else:
               template =  "shortener/already-exists.html"

        return render(request, template, context )



def Kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
    #print(shortcode)

    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    #obj_url = obj.url 
    #try:
     #   obj = KirrURL.objects.get(shortcode=shortcode)
    #except:
     #   obj = KirrURL.objects.all().first()

    #obj_url = None
    #qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
    #if qs.exists() and qs.count() == 1:
    #   obj = qs.first()
    #  obj_url = obj.url 

    return HttpResponseRedirect(obj.url)

class URLRedirectView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)