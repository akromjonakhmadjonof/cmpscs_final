from utils import *


# First validate the date using utils.validate_date
# If the date is valid call save_workout otherwise raise Exception for format
def record_workout(date, exercise_name, weight, reps, sets):
    if not validate_date(date):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD")
    
    # Create the workout row
    row = [date, exercise_name, str(weight), str(reps), str(sets)]
    
    # Save the workout
    save_workout_row(row)
    return True



# Read workouts.csv using utils.read_csv
# Format the data into list of dicts [{....}, {...}]
def load_workouts():
    data = read_csv('workouts.csv')
    
    workouts = []
    for row in data:
        if row: 
            workout_dict = {
                'date': row[0],
                'exercise_name': row[1],
                'weight': float(row[2]),
                'reps': int(row[3]), 
                'sets': int(row[4])
            }
            workouts.append(workout_dict)
    return workouts


# First make sure order of data in row is correct as csv headers and file exists using utils.file_validate
# Save the row using utils.write_csv_row
def save_workout_row(row):
    if len(row) != 5:
        raise ValueError("Row must have 5 elements: date, exercise_name, weight, reps, sets")
    
    file_validate('workouts.csv')
    
    write_csv_row('workouts.csv', row)
    return True


# First call load_workouts to get all data and filter by date to get wanted exercises
def get_workouts_by_date(date):
    if not validate_date(date):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD")
    
    all_workouts = load_workouts()
    
    filtered_workouts = [workout for workout in all_workouts if workout['date'] == date]
    
    return filtered_workouts
