from django.shortcuts import render
from page.models import Slider, Service, Project, Category, Worker, Client

from django.core.context_processors import csrf


def home(request):
    sliders = Slider.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    categories = Category.objects.all()
    workers = Worker.objects.all()
    clients = Client.objects.all()
    context = {}
    context.update(csrf(request))
    context['sliders'] = sliders
    context['services'] = services
    context['projects'] = projects
    context['categories'] = categories
    context['workers'] = workers
    context['clients'] = clients
    return render(request, 'page/home.html', context, request.FILES)
