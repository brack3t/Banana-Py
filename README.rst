========
BananaPy
========

BananaPy provides you with a way to authenticate your Django application with MailChimp's new OAuth2 service.

Installation and Usage
======================

BananaPy requires ``Python-OAuth2`` from SimpleGeo and the ``simplejson`` library, both of which should be installed
automatically if not already installed. You can get BananaPy from its `Github repo <https://github.com/kennethlove/Banana-Py/>` or through PyPi by::

    easy_install banana_py

or::

    pip install banana_py

Let everything install and then set up your MailChimp app. Set the ``redirect uri`` on your MailChimp app to::

    http://your-domain.com/bananas/ripe/

Then add the following four settings to your ``settings.py``::

    INSTALLED_APPS = (
        ...
        'banana_py',
        ...
    )

    MAILCHIMP_CLIENT_ID = '123456789'
    MAILCHIMP_CLIENT_SECRET = 'a1b2c3d4e5f6789'
    MAILCHIMP_REDIRECT_URI = 'http://your-domain.com/bananas/ripe/'
    MAILCHIMP_COMPLETE_URI = 'http://your-domain.com/'

The last setting, ``MAILCHIMP_COMPLETE_URI`` can be anything you want, a Profile page or some view of your own that create 
a user account for the new user.

Add URLs entries::

    urlpatterns = patterns('',
        ...
        url(r'', include('banana_py.urls')),
        ...
    )

In the template(s) where you want to display the authorize link::

    {% load banana_tags %}
    {% banana_auth_url "Authorize" %}

This will print out an HTML anchor tag with the appropriate link and the supplied text as the link text.

Once the user completes the authorization workflow (and ends up on your ``MAILCHIMP_COMPLETE_URI`` view), their
MailChimp-provided authorization information will be available in the ``request.session`` object as ``mailchimp_details``.


Thanks
======

Our thanks to the MailChimp team for letting us build this bridge. Also to Joe Stump and the rest of the SimpleGeo team for making their awesome OAuth2 library. Also, thanks to the Django team, without whom this wouldn't really be needed!

