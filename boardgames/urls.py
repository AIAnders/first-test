from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import SignUpView
from django.contrib.auth.views import login
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('accounts.urls')),
                       url(r'^$', 'main.views.home', name='boardgames_home'),
                       url(r'newGame', 'main.views.newGame', name='newGame'),
                       url(r'newUser', 'accounts.views.SignUpView', name='SignUpView'),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': '/home/dev/boardgames/static'}),
                       url(r'^signup$', SignUpView.as_view(), name='user_signup'),
                       )

urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/', 'login',
        {'template_name': 'login.html'},
        name='boardgames_login'),

    url(r'^logout/', 'logout',
        {'next_page': 'boardgames_home'},
        name='boardgames_logout'),
)
