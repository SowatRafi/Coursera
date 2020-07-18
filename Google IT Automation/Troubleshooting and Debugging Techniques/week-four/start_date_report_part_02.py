#!/usr/bin/env python3


import csv
import os
import datetime

FILE_URL="https://drive.google.com/file/d/1rr_BW7LMsr4smO2OVmAbyDs4NPp9aqGW"
FILE_ID = FILE_URL.split('/')[-1]
FILE_NAME = "employees-with-date.csv"

GET_COOKIE = """curl -c ./cookie -s -L "https://drive.google.com/uc?export=down$
GET_CSV_DATA = """curl -s -Lb ./cookie "https://drive.google.com/uc?export=down$

os.system(GET_COOKIE)

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(file_command):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    os.system(file_command)
    lines = []
    with open(FILE_NAME, encoding = 'UTF-8', mode ='r') as file:
        response = file.readlines()
        for line in response:
            lines.append(line.strip())
        file.close()
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one$
    data = get_file_lines(GET_CSV_DATA)
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in sortedlist:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date >= start_date:
            print("Started on {} : {} {}".format(row_date.strftime("%b %d, %Y")$

def sortedlist():
    start_date = get_start_date()
    sortedlist(start_date)

if __name__ == "sortedlist_":
    sortedlist()
