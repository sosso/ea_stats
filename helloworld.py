from flask import Flask
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

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
