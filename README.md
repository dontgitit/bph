bph
===
A project that allows user to view a graph of earthquakes per day for the past seven days, as well as a list of the ten most recent earthquakes.

This project requires web2py to run. Additionally, it requires the flot.js charting library.
Simply download web2py and unzip. Use "python we2py.py" to run. In web2py/applications, create a symlink to the location of the git repo (so your tree should look like this)
       web2py/applications/bph -> symlink-to-repo-dir/controllers/top10.py
       web2py/applications/bph -> symlink-to-repo-dir/models/top10/index.html

web2py should have made a bunch of folder for you in the repo dir. Unzip the flot.js library into static/js, so your tree looks like this:
       web2py/applications/bph -> symlink-to-repo-dir/static/js/flot/jquery.flot.min.js

To access, go to http://127.0.0.1:8000/bph/top10 or http://127.0.0.1:8000/bph/recent7
