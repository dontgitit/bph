import urllib2
import json
from datetime import datetime, timedelta

def index():
    url_file = urllib2.urlopen("http://www.seismi.org/api/eqs?limit=400")
    json_data = url_file.read()
    results = json.loads(json_data)
    eqs = results['earthquakes']
    # create a list of earthquakes for each day
    days_to_eqs = dict()
    dt = datetime.now()
    for i in range(0, 7):
        dt_str = dt.strftime("%Y-%m-%d")
        days_to_eqs[dt_str] = 0
        dt = dt - timedelta(days = 1)
    for eq in eqs:
        eq_date, eq_time = eq["timedate"].split()
        if eq_date in days_to_eqs:
            days_to_eqs[eq_date] += 1
    return dict(days_to_eqs = days_to_eqs)
