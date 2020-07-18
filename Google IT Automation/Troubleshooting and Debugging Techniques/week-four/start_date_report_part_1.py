#!/usr/bin/env python3

import csv
import os
import datetime

FILE_URL="https://drive.google.com/file/d/1rr_BW7LMsr4smO2OVmAbyDs4NPp9aqGW"
FILE_ID = FILE_URL.split('/') [-1]
FILE_NAME = "employees-with-data.csv"

GET_COOKIE = """curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${file_id}" > /dev/null""".format(file_id = FILE_ID)
GET_CSV_DATA = """curl -s -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/' ./cookie`&id={file_id}" -o {file_name}""".format(file_id = FILE_ID, file_name = FILE_NAME)

os.system(GET_COOKIE)

def get_start_date():
    """Interactively get the start date to query for"""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for year: '))
    month = int(input('Enter a value for month: '))
    day = int(input('Enter a value for day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(file_command):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    os.system(file_command)
    lines = []
    with open(FILE_NAME, encoding = 'UTF-8', mode = 'r') as file:
        reponse = file.readlines()
        for line in reponse:
            line.append(line.strip())
        file.close()
    return lines

def get_same_or_newer(start_date):

    """Returns the employees that started on the given date, or the closest one."""

    data = get_file_lines(GET_CSV_DATA)
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        # If this date is smaller than the one we're looking for,
        # we skip this row

        if row_date < start_date:
            continue

        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimum date.

        if row_date < min_date:
            min_date = row_date
            min_date_employees = []

        # If this date is the same as the current minimum,
        # we add the employees in this row to the list of
        # employees at the minimum date.

        if row_date == min_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))

    return min_date, min_date_employees

def list_newer(start_date):

    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()
