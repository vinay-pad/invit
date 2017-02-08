from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'invit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^events/', include('events.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^membership/', include('membership.urls')),
]
