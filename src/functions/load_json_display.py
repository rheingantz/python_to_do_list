import json
import os
from PySide6.QtWidgets import QListWidgetItem

def load_tasks_from_json(task_list):
    filename = 'data/stored_tasks.json'

    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                task_box = json.load(file)
            task_list.clear()

            for task in task_box:
                item = QListWidgetItem(task["name"])
                task_list.addItem(item)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        task_box = []
        with open(filename, 'w') as file:
            json.dump(task_box, file)

