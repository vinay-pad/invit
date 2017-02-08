from django.conf.urls import include, url, patterns
from users import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
])
