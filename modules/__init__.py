from datetime import datetime

border = "=" * 80

header_tasks = ["Day_name", "Day", "Time", "Task", "Completed"]
current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%I:%M %p")
day_name = datetime.now().strftime("%A")
