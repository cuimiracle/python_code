from django.conf.urls import patterns, include, url
from mysite.views import *
from django.contrib import admin
admin.autodiscover()
from mysite.contact.views import *
from mysite.myapp.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# ('^hello/$', hello),
	# ('^$', my_homepage_view),
	('^time/$', current_datetime),
	# (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^first_app/$', first_app),
    (r'^current_url_view_good/$', current_url_view_good),
    (r'^display_meta/$', display_meta),
    (r'^search_form/$', search_form),
    (r'^search/$', search),
    (r'^contact/$', contact),
    (r'^contact/thanks/$', hello),
    (r'^myapp/$', testFirstReq),
    (r'^myapp/get_news/$', getNews),
    (r'^myapp/add_category/$', addCategory),
    (r'^myapp/publish_news/$', publishNews),
    (r'^myapp/subscribe_news/$', subscribeNews),
    (r'^myapp/desubscribe_news/$', desubscribeNews),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
