from django.shortcuts import render
from django.views import generic
from  scraping.models import news

class Homepageview(generic.ListView):
    template_name='base.html'
    context_object_name = 'articles'
    def get_queryset(self):
        return news.objects.all()