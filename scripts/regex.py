#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  regex.py
#  
#  Copyright 2023 daiana <daiana@reithe>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#800080#  
#  


import re
#log_line = "July 31 07:51.44 mycomputer bad_process: ERROR[00534] Performing package upgrade"
#regex = r"\[(\d+)\]"
#result = re.search(regex, log_line)
#print(result[1])


def extraer_pid(log_line):
    regex = r"\[(\d+)]:\s([A-Z]*)\s"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

extraer_pid("July 31 07:51.44 mycomputer bad_process: ERROR[00734] Performing package upgrade")
