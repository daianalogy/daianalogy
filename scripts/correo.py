#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  email.py
#  
#  Copyright 2023 reithe <reithe@GlaceOS>
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
#  MA 02110-1301, USA.
#  
#  
from email.message import EmailMessage
from mimetypes import MimeTypes
import os.path
import mimetype
import urllib 


mime = MimeTypes()
sender = "me@example.com"
recipient = "you@example.com"
message = EmailMessage()
message['From'] = sender
message['To'] = recipient

#url = urllib.pathname2url('https://docs.python.org/es/3/library/urllib.request.html')
attachment_path = "/home/reithe/Imágenes/youtube-logo-9.png"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = MimeTypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
body = """Hey there!
...
... I'm learning to send emails using Python!"""
message.set_content(body)

print(message)
print(mime_type)
print(mime_subtype)

