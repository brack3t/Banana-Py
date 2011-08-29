from django.conf.urls.defaults import patterns, url
from banana_py.views import BananasCompleteView

urlpatterns = patterns('',
    url(r'^bananas/ripe/$', BananasCompleteView.as_view(), name='bananas_ripe'),
)
