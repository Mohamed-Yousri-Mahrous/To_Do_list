from config import get_current_date, get_current_time, get_day_name
from .file_handler import status_task_line, task_name_line, day_date_line
import csv
from .cli import pause, create_border


def add_task():
    """Add a task to the list."""
    task = input("Enter Name of task: ").strip()
    print(create_border())
    if task:

        with open("tasks.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                [get_day_name(), get_current_date(), get_current_time(), task, False]
            )

        print("\n>> Task added successfully!")
        pause()


def mark_as_completed():
    """Mark a task as completed."""

    print("Available tasks Not Completed yet :")

    # check if tasks.csv has tasks
    with open("tasks.csv", "r", encoding="utf-8") as file:
        tasks = list(csv.reader(file))
        if len(tasks) <= 1:
            print("\n>> No tasks available.")
            pause()
            return

    uncompleted_tasks = [
        task for task in tasks[1:] if task and task[status_task_line] != "True"
    ]

    if not uncompleted_tasks:
        print("\n>> No uncompleted tasks available.")
        pause()
        return

    for index, task in enumerate(uncompleted_tasks, start=1):
        print(f"{index} - {task[task_name_line]}")

    print(create_border())
    try:
        task_index = int(input("Enter Number of task to mark as completed: ").strip())

        if 1 <= task_index <= len(uncompleted_tasks):
            task_to_complete = uncompleted_tasks[task_index - 1]
            for task in tasks:
                if task == task_to_complete:
                    task[status_task_line] = "True"
                    break

            # Write back all tasks
            with open("tasks.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(tasks)
            print("\n>> Task marked as completed Successfully!")
        else:
            print("\n>> Invalid task number.")
    except ValueError:
        print("\n>> Invalid input. Please enter a valid number.")

    pause()


def show_tasks():
    """Display a list of tasks."""
    with open("tasks.csv", "r", encoding="utf-8") as file:
        tasks = list(csv.reader(file))
        if len(tasks) <= 1:
            print("\n>> No tasks available.")
            pause()
            return

    tasks_today = [
        task for task in tasks[1:] if task and task[day_date_line] == get_current_date()
    ]
    if tasks_today:
        print(f"{get_day_name()} - {get_current_date()}", end="\n\n")
        for index, row in enumerate(tasks_today, start=1):
            if row:
                task_size = len(row[task_name_line]) + 8
                print(f"{index} - {row[task_name_line]}", end=" ")
                if row[status_task_line] == "True":
                    print("✅")
                else:
                    print("❌")
                print("=" * task_size if index < len(tasks_today) else "")

    else:
        print(f"\n>> No tasks available for Today.")
    pause()
