import urllib2
import json
from datetime import datetime, timedelta
import calendar

def index():
    url_file = urllib2.urlopen("http://www.seismi.org/api/eqs?limit=100")
    json_data = url_file.read()
    results = json.loads(json_data)
    eqs = results['earthquakes']
    # create a list of earthquakes for each day (keys are milliseconds since midnight in UTC)
    days_to_eqs = dict()
    dt = datetime.utcnow().replace(hour=0, minute=0, second=0)
    for i in range(0, 7):
        #dt_str = dt.strftime("%Y-%m-%d")
        #days_to_eqs[dt_str] = 0
        dt_ms_utc = calendar.timegm(dt.timetuple()) * 1000
        days_to_eqs[dt_ms_utc] = 0
        dt = dt - timedelta(days = 1)
    for eq in eqs:
        eq_date_str, eq_time = eq["timedate"].split()
        eq_dt = datetime.strptime(eq_date_str + " UTC", "%Y-%m-%d %Z")
        eq_ms_utc = calendar.timegm(eq_dt.timetuple()) * 1000
        if eq_ms_utc in days_to_eqs:
            days_to_eqs[eq_ms_utc] += 1
    return dict(days_to_eqs = sorted(days_to_eqs.iteritems()))
