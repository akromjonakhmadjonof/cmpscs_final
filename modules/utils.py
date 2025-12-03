from datetime import datetime
import csv
import os


def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def read_csv(filepath):
    if not os.path.exists(filepath):
        return []

    with open(filepath, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_mdy(date_string):
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    return dt.month, dt.day, dt.year


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


def write_csv_row(filepath, row):
    if not isinstance(row, dict):
        raise Exception("Row has be a dict")

    header_list = list(row.keys())

    file_validate(filepath, header_list)

    with open(filepath, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header_list)
        writer.writerow(row)
