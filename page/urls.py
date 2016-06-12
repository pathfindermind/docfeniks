from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'consulting.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'page.views.home', name='home'),
]
