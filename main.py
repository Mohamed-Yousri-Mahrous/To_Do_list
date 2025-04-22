from modules.task import add_task, mark_as_completed, show_tasks
from modules.file_handler import get_file_info
from modules.cli import clear_screen, pause, welcome, border


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
    main()
