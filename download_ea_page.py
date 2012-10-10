import datetime
import sys
import time
import urllib2

def download_ea_page():
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request('http://www.easportsworld.com/en_US/clubs/partial/401A0001/273/members-list', None, headers)
    stats_page = urllib2.urlopen(req, None, 30).read()
    old_file = open('static/stats_current.html', 'r').read()
    if stats_page != old_file:
        output = open('static/stats_current.html', 'w')
        output.write(stats_page)
        timestring = int(time.mktime(datetime.datetime.now().timetuple()))
        output2 = open('static/%d.html' % timestring, 'w')
        output2.write(stats_page)
        output2.close()
    return 'Downloaded stats'
