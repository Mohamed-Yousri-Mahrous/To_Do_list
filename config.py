from datetime import datetime

# Ui border
border_size = 80


# Program information
program_name = "Task Manager"
program_description = "A simple task manager to help you manage your tasks."


# Function of program that user can use it
fun_list = """      
    1. Add a task
    2. Mark a task as completed
    3. Show tasks
    4. Exit
    """


# Date and time
def get_current_date():
    """Get the current date."""
    return datetime.now().strftime("%d/%m/%Y")


def get_current_time():
    """Get the current time."""
    return datetime.now().strftime("%I:%M %p")


def get_day_name():
    """Get the current day name."""
    return datetime.now().strftime("%A")


# Setting for storage file
header_tasks = ["Day_name", "Day", "Time", "Task", "Completed"]
TASK_FILE = "tasks.csv"
