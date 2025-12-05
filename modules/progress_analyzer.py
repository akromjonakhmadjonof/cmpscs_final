from modules.workout_tracker import *


# Basic math volume = weight * reps * sets.
def calculate_volume(weight, reps, sets):
    try:
        return float(weight) * int(reps) * int(sets)
    except (TypeError, ValueError):
        return 0


# Get workouts using workout_tracker.get_workouts_by_date
# For each exercise in the given day calculate volume using calculate_volume
# Total them all and return total value
def get_daily_volume(date):
    workouts = get_workouts_by_date(date)
    total_volume = 0
    # Loop through each workout and accumulate its volume
    for w in workouts:
        weight = w.get("weight", 0)
        reps = w.get("reps", 0)
        sets = w.get("sets", 0)
        total_volume += calculate_volume(weight, reps, sets)
    return total_volume


# Get all workout records using workout_tracker.load_workouts()
# Gather all unique day like this {"07-12-2025"}. No Duplicates
# And for each day call get_daily_volume(date) and generate arr like this [{date: "02-14-2025", volume: 12000}]
# It is for generating charts later
def get_volume_over_time():
    all_workouts = load_workouts()
    unique_dates = set()
    # Collect each unique date found in the workout records
    for w in all_workouts:
        d = w.get("date")
        if d:
            unique_dates.add(d)
    sorted_dates = sorted(unique_dates)
    result = []
    # Compute volume for each date
    for d in sorted_dates:
        volume = get_daily_volume(d)
        result.append({"date": d, "total_volume": volume})

    return result


# Load all workout records using workout_tracker.load_workouts
# Filter by exercise name
# Find the max_weight and the date to return
def get_max_weight_progress(exercise_name):
    all_workouts = load_workouts()
    max_weight = None
    max_date = None
    # Check every workout
    for w in all_workouts:
        if w.get("exercise") == exercise_name:
            weight = w.get("weight")
            date = w.get("date")
            # Ensure weight exists
            if weight is not None:
                weight = float(weight)
                # Update max if this weight is greater
                if max_weight is None or weight > max_weight:
                    max_weight = weight
                    max_date = date

    if max_weight is None:
        print("No records for this exercise.")
    else:
        print(f"Max weight for {exercise_name}: {max_weight} on {max_date}")
