from utils import *


# First validate the date using utils.validate_date
# If the date is valid call save_workout otherwise raise Exception for format
def record_workout(date, exercise_name, weight, reps, sets):
    pass


# Read workouts.csv using utils.read_csv
# Format the data into list of dicts [{....}, {...}]
def load_workouts():
    pass


# First make sure order of data in row is correct as csv headers and file exists using utils.file_validate
# Save the row using utils.write_csv_row
def save_workout_row(row):
    pass


# First call load_workouts to get all data and filter by date to get wanted exercises
def get_workouts_by_date(date):
    pass
