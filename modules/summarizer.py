from datetime import *
from modules.calorie_tracker import *
from modules.progress_analyzer import *


# Get relevant data from workout, calorie, progress modules to the given date
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
        for w in workouts:
            print(f"  - {w['exercise_name']}: {w['weight']} x {w['reps']} x {w['sets']}")
    else:
        print("No workout recorded.")

    print("Total volume:", total_volume)

    if calories:
        eaten = calories.get("eaten", calories.get("calories_eaten", 0))
        goal = calories.get("goal", calories.get("calorie_goal", 0))
        print(f"Calories: ate {eaten} / goal {goal}")
    else:
        print("No calorie record.")


#  Get relevant data from workout, calorie, progress modules from given start_date
# Call summarize_day 7 times to get summary of each day in the week and calculate totals of them
def summarize_week(start_date):
    m, d, y = get_mdy(start_date)
    start_dt = datetime(y, m, d)

    total_volume = 0
    workout_days = 0

    print(f"\n=== Weekly Summary starting {start_date} ===")

    for i in range(7):
        current = start_dt + timedelta(days=i)
        date_str = current.strftime("%m-%d-%Y")

        print(f"\n--- {date_str} ---")
        day_volume = get_daily_volume(date_str)
        workouts = get_workouts_by_date(date_str)

        if workouts:
            workout_days += 1
            print("Workouts:", len(workouts))
        else:
            print("No workouts.")

        print("Daily volume:", day_volume)

        total_volume += day_volume

    print("\n=== Weekly Results ===")
    print("Total volume:", total_volume)
    print("Workout days:", workout_days)
