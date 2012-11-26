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

from onlinecounter.cache import OnlineCounter


class OnlineCounterMiddleware(object):
    def process_request(self, request):
        self.online_counter = OnlineCounter()
        self.online_counter.delete_idle()
        self.online_counter.check_in(request)
        request.online = self

    def total(self):
        total = len(self.online_counter.online_users)
        return total

    def guest(self):
        guest = len(self.online_counter.guests)
        return guest

    def users(self):
        users = len(self.online_counter.users)
        return users
