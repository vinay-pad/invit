
from django.conf.urls import include, url, patterns
from membership import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$',
        views.MembershipList.as_view(),
        name='membership-list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.MembershipDetail.as_view(),
        name='membership-detail'),
])
