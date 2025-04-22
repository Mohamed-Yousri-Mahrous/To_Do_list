from config import TASK_FILE, header_tasks
import csv
from pathlib import Path

# def load_tasks():
#     try:
#         with open(TASK_FILE, "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []


# def save_tasks(tasks):
#     with open(TASK_FILE, "w") as f:
#         json.dump(tasks, f, indent=2)


def check_tasks_file():
    """
    Check if the tasks file exists.
    """
    task_file_path = Path(TASK_FILE)
    if not Path.exists(task_file_path):
        with open(TASK_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header_tasks)


def get_file_info():
    """
    Get information about the tasks file.
    """
    check_tasks_file()

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = list(csv.reader(file))

        number_of_tasks = len(tasks) - 1
        status_task_line = tasks[0].index("Completed")
        task_name_line = tasks[0].index("Task")
        day_name_line = tasks[0].index("Day_name")
        day_date_line = tasks[0].index("Day")

    return (
        number_of_tasks,
        status_task_line,
        task_name_line,
        day_name_line,
        day_date_line,
    )


number_of_tasks, status_task_line, task_name_line, day_name_line, day_date_line = (
    get_file_info()
)
