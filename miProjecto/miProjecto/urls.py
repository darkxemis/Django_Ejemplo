from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'miProjecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main$', 'main.views.home'),
    url(r'^login$', 'main.views.login'),
    url(r'^register$', 'main.views.register', name='register'),
]
