#   Program Name: main.py
#   Author: Zihui Li
#   Copyright: Penn State University
#   Date: 5 December, 2025

from datetime import *
from modules.calorie_tracker import *
from modules.progress_analyzer import *


# Print a summary for the selected day
def summarize_day(date):
    # load workouts of that day
    workouts = get_workouts_by_date(date)
    # calculate daily total volume
    total_volume = get_daily_volume(date)
    # load calories of that day
    calories = get_calories_by_date(date)

    print(f"\n=== Daily Summary for {date} ===")
    if workouts:
        print("Workouts:")
        # Print each exercise performed on this day
        for w in workouts:
            print(
                f"  - {" ".join(w['exercise_name'].split("_")).capitalize()}: {w['weight']} x {w['reps']} x {w['sets']}")
    else:
        print("No workout recorded.")

    print("Total volume:", total_volume)

    # Show calories eaten vs goal
    if calories:
        eaten = calories.get("eaten", calories.get("calories_eaten", 0))
        goal = calories.get("goal", calories.get("calorie_goal", 0))
        print(f"Calories: ate {eaten} / goal {goal}")
    else:
        print("No calorie record.")


# Summarize 7 days starting from the given date
def summarize_week(start_date):
    m, d, y = get_mdy(start_date)
    start_dt = datetime(y, m, d)

    total_volume = 0
    workout_days = 0
    calorie_goal = 0
    calories_eaten = 0
    cal_diff = calorie_goal - calories_eaten

    print(f"\n=== Weekly Summary starting {start_date} ===")

    # Loop through 7 days
    for i in range(7):
        current = start_dt + timedelta(days=i)
        date_str = current.strftime("%Y-%m-%d")
        day_volume = get_daily_volume(date_str)
        workouts = get_workouts_by_date(date_str)
        calories = get_calories_by_date(date_str)
        # Add daily values to weekly totals
        total_volume += day_volume
        calories_eaten += int(calories["calories_eaten"])
        calorie_goal += int(calories["calorie_goal"])
        if workouts:
            workout_days += 1

        summarize_day(date_str)
    # Compare total eaten vs goal
    if cal_diff > 0:
        msg = f"You are in a deficit of {abs(cal_diff)} kcals"
    elif cal_diff < 0:
        msg = f"You are in a surplus of {abs(cal_diff)} kcals"
    else:
        msg = "You achieved your target!"
    print("\n=== Weekly Results ===")
    print("Calories Status: " + msg)
    print("Total volume:", total_volume)
    print("Workout days:", workout_days)
