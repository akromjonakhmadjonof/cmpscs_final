#   Program Name:   main.py
#
#   Author:         Ye Chen
#
#   Copyright:      Penn State University
#
#   Date:           5 December, 2025
#
#   Description:    This file contains codes that calorie_tracker
from modules.constants import CALORIES
from modules.utils import *


def record_calories(date, calories_eaten, calorie_goal):
    row = {  #Create a dictionary representing the calorie record for the given date
        "date": date,
        "calories_eaten": str(calories_eaten),
        "calorie_goal": str(calorie_goal)
    }

    if save_calorie_row(row):
        print("Calorie entry recorded successfully.\n") #Success
        return True
    print("Something went wrong in saving calories record.\n") #Fails


def load_calories():
    data = read_csv(CALORIES)
    records = []
    for row in data:
        if row: #Convert the CSV row into a standardized dictionary format
            workout_dict = {
                'date': row['date'],
                'calories_eaten': row['calories_eaten'],
                'calorie_goal': row['calorie_goal'],
            }
            records.append(workout_dict) #Add the processed record to the list
    return records


def save_calorie_row(row):
    write_csv_row(CALORIES, row) #Record row to the CSV file
    return True


# Get calories record to given date
def get_calories_by_date(date):
    records = load_calories() #Load all calorie records from the CSV
    data = None
    for record in records:
        if record["date"] == date:
            data = record

    return data
