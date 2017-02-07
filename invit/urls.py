from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Examples:
    # url(r'^$', 'invit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^v1/', include('routerv1.urls')),
]
