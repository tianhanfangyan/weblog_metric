"""
WSGI config for weblog_base project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weblog_base.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
