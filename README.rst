===========
Site Scheme
===========

Site Scheme is a Django app that associates a scheme(HTTP/HTTPS) with a site.

Quick Start
-----------

1. Add "django.contrib.sites" and "sitescheme" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django.contrib.sites',
        ...
        'sitescheme',
    ]


2. Run `python manage.py migrate` to create the sitescheme models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to add a site along with a scheme.
