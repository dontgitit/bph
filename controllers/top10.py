import urllib2
import json

def index():
    url_file = urllib2.urlopen("http://www.seismi.org/api/eqs?limit=10")
    json_data = url_file.read()
    results = json.loads(json_data)
    #count = results['count']
    eqs = results['earthquakes']
    #print "Got %s count" % count
    #for eq in eqs:
    #    print "got eq %s" % eq
    return dict(recent_eqs = eqs)
