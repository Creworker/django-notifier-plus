====================
Installation & Setup
====================

Installation
============

Install via ``pip``.

To download latest dev version:

::

    $ pip install git+git://github.com/scdoshi/django-notifier.git

From PyPI (latest release):

::

    $ pip install django-notifier


Setup
=====

1. Add ``notifier`` to INSTALLED_APPS in your django settings file.

    ::

        INSTALLED_APPS = (
            ...
            'notifier',
            ...
        )

2. Settings

    If you are going to use any custom backends to send notifications, add the setting NOTIFIER_BACKENDS to your settings file. If this setting is not defined, only the EmailBackend is used by default.

    ::

        NOTIFIER_BACKENDS = (
            'notifier.backends.EmailBackend',
            'path.to.custom.backend.CustomBackend',
        )


3. Run ``migrate`` to create the necessary tables in the database.
    
    ::

        $ python manage.py migrate


Terminology
===========

* ``Notification``: A message that can be sent from the system to users (payment declined, email verification).
* ``Backend``: A way to send notifications to users (email, SMS etc.)
