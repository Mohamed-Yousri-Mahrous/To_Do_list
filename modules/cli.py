import os
from modules import border


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
