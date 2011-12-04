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

from django.db import models

class OnlineCounter(models.Model):
    ip = models.IPAddressField(verbose_name="IP Adress", db_column="visitor_ip")
    is_user = models.BooleanField(verbose_name="User ?", db_column="is_user", default=False)
    visited_time = models.TimeField(verbose_name="Visited Time", db_column="visitor_time", auto_now_add=True)

    class Meta:
        db_table = "online_counter"
        verbose_name_plural = "Online Counter"
