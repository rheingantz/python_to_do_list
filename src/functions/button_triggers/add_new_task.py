from src.functions.task_to_json import (save_tasks_to_json)

def add_task(new_task_input):
    new_task_text = new_task_input.text()
    if new_task_text:
        save_tasks_to_json(new_task_text)
        new_task_input.clear()