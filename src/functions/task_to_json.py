import json

def save_tasks_to_json(tasks):
    filename = 'data/stored_tasks.json'
    new_task = {"name": tasks}

    try:
        with open(filename, 'r') as file:
            json_tasks = json.load(file)
    
    except FileNotFoundError:
    
        json_tasks = []

    json_tasks.append(new_task)

    with open(filename, 'w') as file:
        json.dump(json_tasks, file, indent=4)