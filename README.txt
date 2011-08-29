========
BananaPy
========

BananaPy provides you with a way to authenticate your Django application with MailChimp's new OAuth2 service.

Installation and Usage
======================

BananaPy requires ``Python-OAuth2`` from SimpleGeo and the ``simplejson`` library, both of which should be installed automatically if not already installed. You can get BananaPy from it's `Github repo <link here>` or through PyPi by::

    easy_install banana_py

or::

    pip install banana_py

Let everything install and then set up your MailChimp app. Set the ``redirect uri`` on your MailChimp app to::

    http://your-domain.com/bananas/ripe/

Then add the following four settings to your ``settings.py``::

    MAILCHIMP_CLIENT_ID = '123456789'
    MAILCHIMP_CLIENT_SECRET = 'a1b2c3d4e5f6789'
    MAILCHIMP_REDIRECT_URI = 'http://your-domain.com/bananas/ripe/'
    MAILCHIMP_COMPLETE_URI = 'http://your-domain.com/'

The last setting, ``MAILCHIMP_COMPLET_URI`` can be anything you want, a Profile page or some view of your own that create a user account for the new user. 


Thanks
======

Our thanks to the MailChimp team for letting us build this bridge. Also to Joe Stump and the rest of the SimpleGeo team for making their awesome OAuth2 library. Also, thanks to the Django team, without whom this wouldn't really be needed!

