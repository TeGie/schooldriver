#   Copyright 2011 Burke Software and Consulting LLC
#   Author Callista Goss <calli@burkesoftware.com>
#   
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.



from django.conf import settings
import urllib, urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

def queXF(pdf,banding,test_id):
        register_openers()
        url = "http://localhost/trunk/admin/new.php"
        description = "Test_" + str(test_id)
        
        values = {'form':open(pdf, 'r'),
                  'bandingxml':open(banding, 'r'),
                  'desc':description
                  }
        data, headers = multipart_encode(values)
        headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        request = urllib2.Request(url, data, headers)
        request.unverifiable = True
        response = urllib2.urlopen(request)
        the_page = response.read()
