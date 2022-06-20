# Nalaquq


[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg) [![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)



# Directory structure



    .
    ├── app.py                  # runs weather checks and dictionary for drones
    ├── main.py                 # app loader for Kivy
    ├── main.kv                 # .kv markup file for app
    ├── assets                  # contains fonts, background images, and logos for app
    ├── db                      # contains .csv files for airports with long, lat
    ├── requirements		
    └── README.md

# Languages & Dependencies 
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![Vim](https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white)

# APIs  
## Nalaquq relies on the following APIs to generate weather data for flight planning: 

1. Airport locations are are gathered from the FAA's Airport Data and information Portal (ADI). Airport information updated to this portal can be accessed at the following url: 
 
		adip.faa.gov/public/#/airportSearch/advanced

2. Metar and Taf Data are sourced from: 

		https://adip.faa.gov/agis/public/#/airportSearch/advanced 


ssconvert is then used to convert the file to a .csv


