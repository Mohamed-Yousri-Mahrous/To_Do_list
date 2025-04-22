import os


def pause():
    """
    Pause the program until the user presses Enter.
    """
    print(create_border())
    input("Press Enter to continue...")


def welcome(program_name, program_description, fun_list, border_size=80):
    """
    Display a welcome message.
    """
    message = [
        create_border(),
        f" Welcome to the {program_name} program! ".center(border_size, "="),
        f" {program_description} ".center(border_size, "="),
        create_border(),
        fun_list,
        create_border(),
    ]
    print("\n".join(message))


def clear_screen():
    """
    Clear the console screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def create_border(border_size=80):
    """
    Create a border.
    """
    return "=" * border_size
