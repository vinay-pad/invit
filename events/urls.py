from django.conf.urls import include, url, patterns
from events import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$',
        views.EventList.as_view(),
        name='event-list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.EventDetail.as_view(),
        name='event-detail'),
])
