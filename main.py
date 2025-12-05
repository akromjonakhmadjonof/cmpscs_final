from modules import workout_tracker
from modules import calorie_tracker
from modules import summarizer
from modules import chart_creator
from modules import utils


# ----------------------------------------------------------------------
#   Function Name: prompt_date
#   Parameters:   prompt
#   Return Value: date
#   Description:
#    Asks the user to enter the date and checks the format
# ----------------------------------------------------------------------
def prompt_date(prompt="Enter date (YYYY-MM-DD):"):
    while True:
        date = input(prompt).strip()
        if utils.validate_date(date):
            return date
        print("Invalid date format. Please use YYYY-MM-DD.")


# ----------------------------------------------------------------------
#   Function Name: prompt_int
#   Parameters:   prompt_text
#   Return Value: int
#   Description:
#    Asks the user to enter an integer and checks if it is really integer
# ----------------------------------------------------------------------
def prompt_int(prompt_text):
    while True:
        value = input(prompt_text).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer")


# ----------------------------------------------------------------------
#   Function Name: prompt_float
#   Parameters:   prompt_text
#   Return Value: float
#   Description:
#    Asks the user to enter a float and checks if it is really float
# ----------------------------------------------------------------------
def prompt_float(prompt_text):
    while True:
        value = input(prompt_text).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number")


# ----------------------------------------------------------------------
#   Function Name: handle_record_workout
#   Parameters:   None
#   Return Value: None
#   Description:
#    Handles Record Workout section of the menu
# ----------------------------------------------------------------------
def handle_record_workout():
    print("\n====== Record Workout ======")
    date = prompt_date()
    exercise_name = "".join(input("Exercise name: ").strip().lower().split(" "))
    weight = prompt_float("Weight used (e.g., 135): ")
    reps = prompt_int("Reps per set: ")
    sets = prompt_int("Number of sets: ")

    workout_tracker.record_workout(date, exercise_name, weight, reps, sets)
    print("Workout recorded successfully.")


# ----------------------------------------------------------------------
#   Function Name: handle_record_calories
#   Parameters:   None
#   Return Value: None
#   Description:
#    Handles Record Calories section of the menu
# ----------------------------------------------------------------------
def handle_record_calories():
    print("\n====== Record Calories ======")
    date = prompt_date()
    calories_eaten = prompt_int("Calories eaten: ")
    calorie_goal = prompt_int("Calorie goal: ")

    calorie_tracker.record_calories(date, calories_eaten, calorie_goal)


# ----------------------------------------------------------------------
#   Function Name: handle_daily_summary
#   Parameters:   None
#   Return Value: None
#   Description:
#    Handles Record Daily Summary section of the menu
# ----------------------------------------------------------------------
def handle_daily_summary():
    print("\n====== Daily Summary ======")
    date = prompt_date()
    summarizer.summarize_day(date)


# ----------------------------------------------------------------------
#   Function Name: handle_weekly_summary
#   Parameters:   None
#   Return Value: None
#   Description:
#    Handles Weekly Summary section  of the menu
# ----------------------------------------------------------------------
def handle_weekly_summary():
    print("\n====== Weekly Summary ======")
    start_date = prompt_date("Enter the start date of the week (YYYY-MM-DD): ")
    summarizer.summarize_week(start_date)


# ----------------------------------------------------------------------
#   Function Name: handle_generate_chart
#   Parameters:   None
#   Return Value: None
#   Description:
#    Handles Generate Chart section of the menu
# ----------------------------------------------------------------------
def handle_generate_chart():
    print("\n====== Generate Chart=== ===")
    print("1. Generate workout volume chart")
    print("2. Generate calorie chart")
    print("3. Generate combined chart")
    print("4. Back to main menu")

    choice = int(input("Choose an option: ").strip())

    if choice == 1:
        filepath = chart_creator.generate_volume_chart()
        print(f"Volume chart saved at: {filepath}\n")
    elif choice == 2:
        filepath = chart_creator.generate_calorie_chart()
        print(f"Calorie chart saved at: {filepath}\n")
    elif choice == 3:
        filepath = chart_creator.generate_combined_chart()
        print(f"Combined chart saved at: {filepath}\n")
    elif choice == 4:
        print()
        return
    else:
        print("Invalid choice. Returning to main menu.\n")


# ----------------------------------------------------------------------
#   Function Name: main
#   Parameters:   None
#   Return Value: None
#   Description:
#    Runs the program
# ----------------------------------------------------------------------
def main():
    while True:
        print("=== Fitness Tracker Menu ===")
        print("1. Record Workout")
        print("2. Record Calories")
        print("3. View Daily Summary")
        print("4. View Weekly Summary")
        print("5. Generate Summary Charts")
        print("6. Exit")

        choice = int(input("Choose an option: ").strip())

        if choice == 1:
            handle_record_workout()
        elif choice == 2:
            handle_record_calories()
        elif choice == 3:
            handle_daily_summary()
        elif choice == 4:
            handle_weekly_summary()
        elif choice == 5:
            handle_generate_chart()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


main()
