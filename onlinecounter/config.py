# coding: utf-8
from django.conf import settings

ONLINE_USER_TIMEOUT = getattr(settings, 'ONLINE_USER_TIMEOUT', 5 * 60)
ONLINE_USERS_KEY = getattr(settings, 'ONLINE_USERS_KEY', 'online_users_%d' % settings.SITE_ID)
ONLINE_USER_KEY_PREFIX = getattr(settings, 'ONLINE_USER_KEY_PREFIX', ONLINE_USERS_KEY)
