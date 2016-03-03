from django.conf.urls import include, url
from django.contrib import admin
from climate.views import view

urlpatterns = [
    # Examples:
    # url(r'^$', 'yale_climate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view, name='view'),
]
