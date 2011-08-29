from django import template

from banana_py import Bananas_OAuth

register = template.Library()

@register.simple_tag
def banana_auth_url(link_text):
    return u'<a href="%s">%s</a>' % (Bananas_OAuth().authorize_url(), link_text)
