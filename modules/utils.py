#   Program Name:   main.py
#
#   Author:         Akromjon Akhmadjonov
#
#   Copyright:      Penn State University
#
#   Date:           5 December, 2025
#
#   Description:    This file contains shared functions all over project
from datetime import datetime
import csv
import os


# ----------------------------------------------------------------------
#   Function Name: validate_date
#   Parameters:   prompt_text: string
#   Return Value: Boolean
#   Description:
#    Checks if the given date is formatted
# ----------------------------------------------------------------------
def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ----------------------------------------------------------------------
#   Function Name: read_csv
#   Parameters:   filepath: string
#   Return Value: Boolean
#   Description:
#    Checks if the given date is formatted
# ----------------------------------------------------------------------
def read_csv(filepath):
    if not os.path.exists(filepath):
        return []

    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


# ----------------------------------------------------------------------
#   Function Name: get_mdy
#   Parameters:   date_string: string
#   Return Value: str, str, str
#   Description:
#    Separates the day, month, year from given date string
# ----------------------------------------------------------------------
def get_mdy(date_string):
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    return dt.month, dt.day, dt.year


# ----------------------------------------------------------------------
#   Function Name: file_validate
#   Parameters:   filepath: string, header_list [str]
#   Return Value: None
#   Description:
#    checks if the csv file in filepath exists and is correct otherwise it corrects it
# ----------------------------------------------------------------------
def file_validate(filepath, header_list):
    if not os.path.exists(filepath):
        with open(filepath, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header_list)
        return

    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        try:
            existing_headers = next(reader)
        except Exception:
            existing_headers = []

    if existing_headers != header_list:
        with open(filepath, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header_list)


# ----------------------------------------------------------------------
#   Function Name: write_csv_row
#   Parameters:   filepath: string, row: dict
#   Return Value: None
#   Description:
#    Saves the row to the csv file in the given filepath
# ----------------------------------------------------------------------
def write_csv_row(filepath, row):
    if not isinstance(row, dict):
        raise Exception("Row has be a dict")

    header_list = list(row.keys())

    file_validate(filepath, header_list)

    with open(filepath, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header_list)
        writer.writerow(row)
