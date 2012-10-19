from flask import Flask, request
import download_ea_page
import os

app = Flask(__name__)

@app.route('/showstats')
def hello():
#    self.response.headers['Content-Type'] = 'text/html'
#    self.response.out.write()
    return open('static/stats_current.html').read()
#    return app.send_static_file('static/stats_current.html')

@app.route('/fetchstats')
def fetch_stats():
#    self.response.headers['Content-Type'] = 'text/plain'
#    self.response.out.write(download_ea_page.download_ea_page())
    return download_ea_page.download_ea_page()

@app.route('/oldstats')
def serve_old_stats():
    oldpages = os.listdir('static')
    oldpages.sort()
    if request.args['filename'] in oldpages:
        return open('static/%s' % request.args['filename']).read()
    else:
        links_html = ''
        for filename in oldpages:
            links_html += '<a href=http://ea-stats.herokuapp.com/oldstats?filename="%s">%s</a><br>' % (filename, filename)

        return_html = '<html><body>' + links_html + '<body></html>'
        return return_html

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
