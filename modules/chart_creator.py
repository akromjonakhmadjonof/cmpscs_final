import matplotlib.pyplot as plt

from modules.progress_analyzer import *
from modules.calorie_tracker import *


# ----------------------------------------------------------------------
#   Function Name: parse_date
#   Parameters:   date: string
#   Return Value: date: string formatted date
#   Description:
#    Formats and Parses the given date
# ----------------------------------------------------------------------
def parse_date(date):
    return datetime.strptime(date, "%Y-%m-%d").date()


# ----------------------------------------------------------------------
#   Function Name: sort_by_date
#   Parameters:   list_of_dicts: [{}]
#   Return Value:  list_of_dicts: [{}]
#   Description:
#    Formats the list of dicts
# ----------------------------------------------------------------------
def sort_by_date(list_of_dicts):
    def get_date_value(item):
        return parse_date(item["date"])

    return sorted(list_of_dicts, key=get_date_value)


# ----------------------------------------------------------------------
#   Function Name: generate_volume_chart
#   Parameters:  None
#   Return Value:  saved file path
#   Description:
#    Generates Volume Chart
# ----------------------------------------------------------------------
def generate_volume_chart():
    data = get_volume_over_time()

    if len(data) == 0:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, "No workout data available", ha="center", va="center")
        ax.set_axis_off()

        return save_chart(fig, VOLUME_CHART)

    data_sorted = sort_by_date(data)

    dates = []
    volumes = []

    for item in data_sorted:
        dates.append(item["date"])
        volumes.append(item["total_volume"])

    fig, ax = plt.subplots()

    ax.plot(dates, volumes, marker="o")
    ax.set_title("Workout Volume Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Volume")

    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()

    return save_chart(fig, VOLUME_CHART)


# ----------------------------------------------------------------------
#   Function Name: generate_calorie_chart
#   Parameters:  None
#   Return Value:  saved file path
#   Description:
#    Generates Calories Chart
# ----------------------------------------------------------------------
def generate_calorie_chart():
    entries = load_calories()

    if len(entries) == 0:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, "No calorie data available", ha="center", va="center")
        ax.set_axis_off()

        return save_chart(fig, CALORIES_CHART)

    entries_sorted = sort_by_date(entries)

    dates = []
    calories_eaten = []
    calorie_goals = []

    for row in entries_sorted:
        dates.append(row["date"])
        calories_eaten.append(int(row["calories_eaten"]))
        calorie_goals.append(int(row["calorie_goal"]))

    fig, ax = plt.subplots()

    ax.plot(dates, calories_eaten, marker="o", label="Calories Eaten")
    ax.plot(dates, calorie_goals, marker="x", linestyle="--", label="Calorie Goal")

    ax.set_title("Calories vs. Calorie Goal")
    ax.set_xlabel("Date")
    ax.set_ylabel("Calories")

    ax.tick_params(axis="x", rotation=45)
    ax.legend()
    fig.tight_layout()

    return save_chart(fig, CALORIES_CHART)


# ----------------------------------------------------------------------
#   Function Name: generate_combined_chart
#   Parameters:  None
#   Return Value:  saved file path
#   Description:
#    Generates Combined Chart
# ----------------------------------------------------------------------
def generate_combined_chart():
    volume_data = get_volume_over_time()
    calorie_data = load_calories()

    if len(volume_data) == 0 and len(calorie_data) == 0:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, "No data available", ha="center", va="center")
        ax.set_axis_off()

        return save_chart(fig, COMBINED_CHART)

    volume_map = {}
    for item in volume_data:
        date = item["date"]
        volume_map[date] = item["total_volume"]

    calorie_map = {}
    for item in calorie_data:
        date = item["date"]
        calorie_map[date] = int(item["calories_eaten"])

    all_dates = []
    for date in volume_map.keys():
        if date not in all_dates:
            all_dates.append(date)

    for date in calorie_map.keys():
        if date not in all_dates:
            all_dates.append(date)

    all_dates.sort(key=parse_date)

    volumes = []
    for date in all_dates:
        if date in volume_map:
            volumes.append(volume_map[date])
        else:
            volumes.append(0)

    calories = []
    for date in all_dates:
        if date in calorie_map:
            calories.append(calorie_map[date])
        else:
            calories.append(0)

    x_positions = []
    for i in range(len(all_dates)):
        x_positions.append(i)

    fig, ax1 = plt.subplots()

    ax1.bar(x_positions, volumes, alpha=0.6)
    ax1.set_ylabel("Total Volume")
    ax1.set_xlabel("Date")

    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(all_dates, rotation=45, ha="right")

    ax2 = ax1.twinx()
    ax2.plot(x_positions, calories, marker="o", color="red")
    ax2.set_ylabel("Calories Eaten")

    fig.suptitle("Volume & Calories Over Time")
    fig.tight_layout()

    return save_chart(fig, COMBINED_CHART)


# Saves the generated file to given filepath
def save_chart(fig, filepath):
    if os.path.exists(filepath):
        os.remove(filepath)

    folder = os.path.dirname(filepath)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    fig.savefig(filepath, bbox_inches="tight")
    plt.close(fig)

    return filepath
