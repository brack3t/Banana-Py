"""
BananaPy provides you with a way to authenticate your Django application with MailChimp's new OAuth2 service.
"""
version = (0, 1, 1)
__version__ = '.'.join(map(str, version))


from django.conf import settings
from django.template.defaultfilters import urlencode
from django.core.exceptions import ImproperlyConfigured

import oauth2 as oauth
import simplejson


class Bananas_OAuth(object):
    mc_authorize_uri = 'https://login.mailchimp.com/oauth2/authorize'
    mc_access_token_uri = 'https://login.mailchimp.com/oauth2/token'
    mc_metadata_uri = 'https://login.mailchimp.com/oauth2/metadata'

    def __init__(self, *args, **kwargs):
        self.client_id = getattr(settings, 'MAILCHIMP_CLIENT_ID', None)
        self.client_secret = getattr(settings, 'MAILCHIMP_CLIENT_SECRET', None)
        self.redirect_uri = getattr(settings, 'MAILCHIMP_REDIRECT_URI', None)
        self.client = oauth.Client(oauth.Consumer(key=self.client_id,
            secret=self.client_secret))

        if not self.client_id:
            raise ImproperlyConfigured("Missing Client ID settings.")
        if not self.client_secret:
            raise ImproperlyConfigured("Missing Client Secret")
        if not self.redirect_uri:
            raise ImproperlyConfigured("Missing Redirect URI")

    def _params(self, code):
        return u'grant_type=%s&code=%s&redirect_uri=%s&client_id=%s&client_secret=%s' % (
            'authorization_code', code, self.redirect_uri, self.client_id,
            self.client_secret)

    def _magic_header(self, token):
        """
        From Mail Chimps docs. This header is the 'magic' that makes this
        empty GET request work.
        """
        return {'Authorization': 'OAuth %s' % token}

    def authenticate(self, code):
        response = {}
        resp, content = self.client.request(self.mc_access_token_uri,
            'POST', self._params(code))
        response.update(simplejson.loads(content))

        resp, content = self.client.request(self.mc_metadata_uri,
            'GET', headers=self._magic_header(response['access_token']))
        response.update(simplejson.loads(content))

        return response

    def authorize_url(self):
        return u'%s?response_type=code&client_id=%s&redirect_uri=%s' % (
            self.mc_authorize_uri, self.client_id, urlencode(self.redirect_uri))
