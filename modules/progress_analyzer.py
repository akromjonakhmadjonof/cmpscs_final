from utils import *
from workout_tracker import *


# Basic math volume = weight * reps * sets.
def calculate_volume(weight, reps, sets):
    pass


# Get workouts using workout_tracker.get_workouts_by_date
# For each exercise in the given day calculate volume using calculate_volume
# Total them all and return total value
def get_daily_volume(date):
    pass


# Get all workout records using workout_tracker.load_workouts()
# Gather all unique day like this {"07-12-2025"}. No Duplicates
# And for each day call get_daily_volume(date) and generate arr like this [{date: "02-14-2025", volume: 12000}]
# It is for generating charts later
def get_volume_over_time():
    pass


# Load all workout records using workout_tracker.load_workouts
# Filter by exercise name
# Find the max_weight and the date to return
def get_max_weight_progress(exercise_name):
    pass
