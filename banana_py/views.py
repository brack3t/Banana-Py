from django.conf import settings
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

from banana_py import Bananas_OAuth


class BananasCompleteView(TemplateView):
    template_name = 'banana_py/fail.html'

    def get(self, request):
        try:
            code = request.GET['code']
        except KeyError:
            error = request.GET.get('error', None)
            return self.render_to_response({'error': error})

        bananas = Bananas_OAuth().authenticate(code)
        request.session['mailchimp_details'] = bananas

        return HttpResponseRedirect(settings.MAILCHIMP_COMPLETE_URI)
