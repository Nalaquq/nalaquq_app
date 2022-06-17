#Nalaquq


[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)

[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

# Directory structure
.
├── app.py                  # runs weather checks and dictionary for drones
├── main.py                 # app loader for Kivy
├── main.kv                 # .kv markup file for app
├── assets                  # contains fonts, background images, and logos for app
├── db                      # contains .csv files for airports with long, lat
├── requirements		
└── README.md

# Python !
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# APIs  
## Nalaquq relies on the following APIs to generate weather data for flight planning: 
1. Airport Databases are updated  
the airport database is gathered from the following URL: 
adip.faa.gov/public/#/airportSearch/advanced
ssconvert is then used to convert the file to a .csv

