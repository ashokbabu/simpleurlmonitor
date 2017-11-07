# simpleurlmonitor

Simple python code is a program that monitors web sites and reports their availability, to a Log file.

Main functions: 
- Reads a list of weburls and corresponding page content requirements from the configuration file.
- Periodically makes a request to all urls as per setting in configuration file (configuration.cfg).
- Verifies that the page content received from the web server matches the content requirements.
- Measures the time it took for the web server to complete the each url request.
- Writes to a log file that shows the progress of the periodic checks.

Usage:
------
python monitor.py

For every 15 seconds,  statuses all urls are reported to a log file (websitemonitor.log), in the same directory.

Log File Format

<TIMESTAMP> WEB URL: <URLTESTED> SearchKey:<ContentSearch> WEBURL STATUS:<UP/DOWN> CONTENT FOUND:<TRUE/FALSE> Time Taken:<T> seconds

UP   - Wesbite is up and running
DOWN - Wesbite is down and not running

Content Verification if found then CONTENT FOUND IS TRUE ELSE FALSE.
Time Taken : Time took to complete the url request.

Ex:
INFO:root:	2016/09/26 22:01:43	WEB URL: https://www.facebook.com SearchKey:email WEBURL STATUS:UP CONTENT FOUND:True Time Taken:0.298578023911 seconds

Contact: chashokbabu@gmail.com