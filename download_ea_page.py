import datetime
import sys
import time
import urllib2

def download_ea_page():
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request('http://www.easportsworld.com/en_US/clubs/partial/401A0001/273/members-list', None, headers)
    stats_page = urllib2.urlopen(req, None, 30).read()
    output = open('stats_current.html', 'wb')
    output.write(stats_page.content)
    output.close()
    output2 = open('%s.html' % time.mktime(datetime.datetime.now().timetuple(), 'wb'))
    output2.write(stats_page)
    output2.close()
    return 'Downloaded stats'
