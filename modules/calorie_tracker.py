from modules.constants import CALORIES
from modules.utils import *


def record_calories(date, calories_eaten, calorie_goal):
    row = {
        "date": date,
        "calories_eaten": str(calories_eaten),
        "calorie_goal": str(calorie_goal)
    }

    if save_calorie_row(row):
        print("Calorie entry recorded successfully.\n")
        return True
    print("Something went wrong in saving calories record.\n")


def load_calories():
    data = read_csv(CALORIES)
    records = []
    for row in data:
        if row:
            workout_dict = {
                'date': row['date'],
                'calories_eaten': row['calories_eaten'],
                'calorie_goal': row['calorie_goal'],
            }
            records.append(workout_dict)
    return records


def save_calorie_row(row):
    write_csv_row(CALORIES, row)
    return True


# Get calories record to given date
def get_calories_by_date(date):
    records = load_calories()
    data = None
    for record in records:
        if record["date"] == date:
            data = record

    return data
