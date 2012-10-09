from google.appengine.api import urlfetch
import datetime
import time

def download_ea_page():
    stats_page = urlfetch.fetch(url="http://www.easportsworld.com/en_US/clubs/partial/401A0001/273/members-list",
                                method=urlfetch.GET)
    if stats_page.status_code == 200:
        output = open('stats_current.html', 'wb')
        output.write(stats_page.content)
        output.close()
        output2 = open('%s.html' % time.mktime(datetime.datetime.now().timetuple(), 'wb'))
        output2.write(stats_page)
        output2.close()
        return 'Downloaded stats'
    else:
        return 'Failed'
