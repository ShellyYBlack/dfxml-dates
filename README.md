# DFXML date report

This script creates a CSV with the filename, mtime, and ctime for each <fileobject> element in a [DFXML file](https://github.com/dfxml-working-group/dfxml_python).

1. Install Beautiful Soup and the lxml toolkit. If you're using Python 3 on Mac or Windows, run `pip3 install beautifulsoup4 lxml`. If you're on Linux, run `sudo apt-get install python3-bs4 python3-lxml`.
2. Change to the directory containing your DFXML.
3. Run the script: `python3 dfxml-dates.py`
4. Open dfxml-dates.csv in Excel and sort the columns to find the earliest date.