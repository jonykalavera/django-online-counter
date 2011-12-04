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

from onlinecounter.models import OnlineCounter
from datetime import datetime, time

class OnlineCounterMiddleware(object):
    def process_request(self, request):
        now_time = datetime.now().time()
        limit = time(now_time.hour, now_time.minute-5, now_time.second, now_time.microsecond)
        OnlineCounter.objects.filter(visited_time__lt=limit).delete()
        online, create = OnlineCounter.objects.get_or_create(ip=request.META["REMOTE_ADDR"])
        if request.user.is_authenticated():
            online.is_user = True
        if not create:
            online.is_user = False
            online.visited_time = now_time
            online.save()
        request.online = self

    def total(self):
        total = OnlineCounter.objects.all().count()
        return total

    def guest(self):
        guest = OnlineCounter.objects.filter(is_user=False).count()
        return guest

    def users(self):
        users = OnlineCounter.objects.filter(is_user=True).count()
        return users
