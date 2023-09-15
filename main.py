import sys
from src.interface_display.user_interface import InitialPage
from src.functions.load_json_display import load_tasks_from_json
from src.functions.button_triggers.add_new_task import add_task
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication([])
    initial_interface = InitialPage()
    load_tasks_from_json(initial_interface.ui.view_box)

    def add_task_and_refresh():
        add_task(initial_interface.ui.new_task_input_line)
        load_tasks_from_json(initial_interface.ui.view_box)

    initial_interface.ui.add_task_button.clicked.connect(add_task_and_refresh)
    initial_interface.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()