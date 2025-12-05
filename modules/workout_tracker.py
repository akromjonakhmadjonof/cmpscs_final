#   Program Name:   main.py
#
#   Author:         Ye Chen
#
#   Copyright:      Penn State University
#
#   Date:           5 December, 2025
#
#   Description:    This file contains codes that workout tracker
from modules.constants import * 
from modules.utils import *


# First validate the date using utils.validate_date
# If the date is valid call save_workout otherwise raise Exception for format
def record_workout(date, exercise_name, weight, reps, sets):
    # Create the workout row
    row = {
        'date': date,
        'exercise_name': "".join(exercise_name.split(" ")),
        'weight': str(weight),
        'reps': str(reps),
        'sets': str(sets)
    }

    # Save the workout
    save_workout_row(row)
    return True


# Read workouts.csv using utils.read_csv
# Format the data into list of dicts [{....}, {...}]
def load_workouts():
    data = read_csv(WORKOUTS)
    workouts = []
    for row in data:
        if row:
            workout_dict = {
                'date': row['date'],
                'exercise_name': row['exercise_name'],
                'weight': float(row['weight']),
                'reps': int(row['reps']),
                'sets': int(row['sets'])
            }
            workouts.append(workout_dict)
    return workouts


# First make sure order of data in row is correct as csv headers and file exists using utils.file_validate
# Save the row using utils.write_csv_row
def save_workout_row(row):
    if len(row) != 5:
        raise ValueError("Row must have 5 elements: date, exercise_name, weight, reps, sets")

    write_csv_row(WORKOUTS, row)
    return True


# First call load_workouts to get all data and filter by date to get wanted exercises
def get_workouts_by_date(date):
    all_workouts = load_workouts()

    filtered_workouts = [workout for workout in all_workouts if workout['date'] == date]

    return filtered_workouts
