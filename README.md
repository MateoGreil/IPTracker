# IPTracker
Script who send you an email if your public IP change.
Add this script in your crontab ! Example (execute the script all the 6 hours) :
0 */6 * * * cd /path/to/IPTracker && /usr/bin/python3 /path/to/IPTracker/ip_tracker.py >> /path/to/IPTracker/ip_tracker.log

This script work only with Gmail.

Make your config.py file with the config.example.
