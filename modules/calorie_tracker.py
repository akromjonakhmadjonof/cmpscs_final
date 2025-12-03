from utils import *


# Validate the date using utils.validate_date if the date exists overwrite it
def record_calories(date, calories_eaten, calorie_goal):
    # Check if date is valid
    if not validate_date(date):
        print("Error: Invalid date. Use YYYY-MM-DD")
        return False
    
    # Create the row to save
    row = [date, str(calories_eaten), str(calorie_goal)]
    
    save_calorie_row(row)
    return True
    
# Load all records from calories.csv
def load_calories():
    records = []
    file = None
    file = open('calories.csv', 'r')
    if file:
        lines = file.readllines()
        file.close()
        records = [line.strip().split(',') for line in lines if line.strip()]
    return records


# Save the row using utils.write_csv_row
def save_calorie_row(row):
    with open('calories.csv', 'a') as file:
        file.write(','.join(row) + '\n')
    return True


# Get calories record to given date
def get_calories_by_date(date):
    records = load_calories()
    
    # Look for matching date
    for record in records:
        if record[0] == date:
            # Found it!
            return {
                'date': record[0],
                'calories_eaten': record[1],
                'calorie_goal': record[2]
            }
    
    return None
