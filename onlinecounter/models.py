#-*- coding:utf-8 -*-

#Copyright (C) 2011, Metehan Özbek
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
from datetime import datetime, timedelta
import time

from django.contrib.auth.models import User
from django.core import cache

from .config import ONLINE_USERS_KEY, ONLINE_USER_KEY_PREFIX, \
    ONLINE_USER_TIMEOUT


class OnlineCounter(object):
    def online_users():
        doc = "The online_users property."

        def fget(self):
            if not getattr(self, '_online_users', False):
                self._online_users = cache.get(ONLINE_USERS_KEY, {})
            return self._online_users

        def fset(self, value):
            cache.set(ONLINE_USERS_KEY, value)
            self._online_users = value

        def fdel(self):
            cache.delete(ONLINE_USERS_KEY)
            del self._online_users
        return locals()
    online_users = property(**online_users())

    @property
    def guests(self):
        if not getattr(self, '_guests', False):
            self._guests = dict(
                (k, v) for k, v in self.online_users if not v.get(
                    'is_user', False))
        return self._guests

    @property
    def users(self):
        if not getattr(self, '_users', False):
            self._users = dict(
                (k, v) for k, v in self.online_users if v.get(
                    'is_user', False))
        return self._users

    def delete_idle(self):
        limit = datetime.now() - timedelta(seconds=ONLINE_USER_TIMEOUT)
        limit_ts = time.mktime(limit.timetuple())
        self._online_users = dict(
            (k, v) for k, v in self.online_users if v.get(
                'visited_time') > limit_ts)

    def check_in(self, request):
        now_ts = time.mktime(datetime.now().timetuple())
        online_user = self.online_users.get(request.session.id, {})
        if request.user.is_authenticated():
            online_user['is_user'] = True
            cache.set(
                '%s_%s' % (
                    ONLINE_USER_KEY_PREFIX,
                    str(request.user.pk)
                ), True, ONLINE_USER_TIMEOUT)
        else:
            online_user['is_user'] = False
        online_user['visited_time'] = now_ts
        self.online_users[request.session.id] = online_user


def patch_user():
    def is_online(self):
        return cache.get(
            '%s_%s' % (ONLINE_USER_KEY_PREFIX, str(self.pk)), False)
    User.is_online = is_online


if not getattr(User, 'is_online', False):
    patch_user()
