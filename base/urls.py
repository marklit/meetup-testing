from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'candidate.views.create', name='create'),
    url(r'^thanks/', 'candidate.views.created', name='created'),
)
