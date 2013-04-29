bph
===
A project that allows user to view a graph of earthquakes per day for the past seven days, as well as a list of the ten most recent earthquakes.

This project requires web2py to run. 
Simply download web2py and unzip. Use "python we2py.py" to run. In web2py/applications, create a symlink to the location of the git repo (so your tree should look like this)
       web2py/applications/bph -> symlink-to-repo-dir/controllers/top10.py
       web2py/applications/bph -> symlink-to-repo-dir/models/top10/index.html

To access, go to http://127.0.0.1:8000/bph/top10