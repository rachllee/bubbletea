import os
from pyicloud import PyiCloudService
from datetime import datetime, timezone, timedelta
import subprocess

api = PyiCloudService('r8chel18164@gmail.com')
date_modified = api.drive['bubbletea']['orders.txt'].date_modified

def convert_to_full_month(month_num):
    months = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    return months.get(month_num, 'Invalid Month')

date_modified_est = date_modified.astimezone(timezone(timedelta(hours=-5)))
month_num = date_modified_est.month

month = convert_to_full_month(month_num)
day = date_modified_est.day
year = date_modified_est.year

time = date_modified_est.strftime('%Y-%m-%d %I:%M:%S %p')

subprocess.run(['python3', 'calc.py', month, day, year, time])
