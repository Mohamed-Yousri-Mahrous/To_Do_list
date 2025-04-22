import os
from pathlib import Path
from datetime import datetime
import csv


def add_task():
    """Add a task to the list."""
    task = input("Enter Name of task: ").strip()
    print(border)
    if task:

        with open("tasks.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([day_name, current_date, current_time, task, False])

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

    print(border)
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
        task for task in tasks[1:] if task and task[day_date_line] == current_date
    ]
    if tasks_today:
        print(f"{day_name} - {current_date}", end="\n\n")
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


def pause():
    """
    Pause the program until the user presses Enter.
    """
    print(border)
    input("Press Enter to continue...")


def welcome():
    """
    Display a welcome message.
    """
    message = [
        border,
        " Welcome to the To Do List program! ".center(80, "="),
        " This program allows you to manage your tasks.".center(80, "="),
        border,
    ]

    fun_list = """      
    1. Add a task
    2. Mark a task as completed
    3. Show tasks
    4. Exit
    """

    message.append(fun_list)
    message.append(border)

    print("\n".join(message))


def clear_screen():
    """
    Clear the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def check_tasks_file():
    """
    Check if the tasks file exists.
    """
    task_file_path = Path("tasks.csv")
    if not Path.exists(task_file_path):
        with open("tasks.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(header_tasks)


def get_file_info():
    """
    Get information about the tasks file.
    """
    check_tasks_file()

    with open("tasks.csv", "r", encoding="utf-8") as file:
        tasks = csv.reader(file)
        tasks = list(tasks)
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


def main():
    """
    Main function to run the To Do List program.
    """

    tasks = {
        "1": add_task,
        "2": mark_as_completed,
        "3": show_tasks,
    }
    while True:
        clear_screen()
        get_file_info()
        welcome()
        choice = input("Enter Number from Function List: ").strip()
        print(border)

        if choice == "4":
            break
        elif choice in tasks:
            tasks[choice]()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    number_of_tasks, status_task_line, task_name_line, day_name_line, day_date_line = (
        get_file_info()
    )
    border = "=" * 80
    header_tasks = ["Day_name", "Day", "Time", "Task", "Completed"]
    current_date = datetime.now().strftime("%d/%m/%Y")
    current_time = datetime.now().strftime("%I:%M %p")
    day_name = datetime.now().strftime("%A")
    main()
