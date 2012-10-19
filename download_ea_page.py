import datetime
import httplib
import logging
import sys
import time
import urllib2

logger = logging.getLogger('tcpserver')

def download_ea_page():
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request('http://www.easportsworld.com/en_US/clubs/partial/401A0001/273/members-list', None, headers)
    try:
        stats_page = urllib2.urlopen(req, None, 30).read()
        print('Stats downloaded successfully')
    except urllib2.HTTPError, e:
        print('HTTPError = ' + str(e.code))
    except urllib2.URLError, e:
        print('URLError = ' + str(e.reason))
    except httplib.HTTPException, e:
        print('HTTPException')
    except Exception:
        import traceback
        print('generic exception: ' + traceback.format_exc())
        print('Unable to fetch page')
    old_file = open('./static/stats_current.html', 'r').read()
    if stats_page != old_file:
        print('stats changed, writing new file')
        output = open('static/stats_current.html', 'w')
        output.write(stats_page)
        output.close()
        timestring = int(time.mktime(datetime.datetime.now().timetuple()))
        output2 = open('static/%d.html' % timestring, 'w')
        output2.write(stats_page)
        output2.close()
    else:
        print('stats did not change, not writing new file')
    return 'Complete'
