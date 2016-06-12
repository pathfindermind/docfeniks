from django.contrib import admin
from page.models import Slider, Service, Project, Category, Worker, Client

admin.site.register([Slider, Service, Category, Worker, Client])

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    radio_fields = {"category": admin.VERTICAL}

admin.site.register(Project, ProjectAdmin)
