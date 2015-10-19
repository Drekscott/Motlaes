from django.shortcuts import render
from store import models
from django.views.generic.base import TemplateView
# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about_mot'] = About.objects.all()
        return context