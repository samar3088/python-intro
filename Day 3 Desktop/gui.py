import FreeSimpleGUI

import functions
import FreeSimpleGUI as sg

# https://pypi.org/

label = sg.Text("Type a TODO")
input_box = FreeSimpleGUI.InputText(tooltip="Enter TODO", key="todo")
add_button = sg.Button("Add")

window = sg.Window('My TODO Window',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica',12))

while True:
    event,values = window.read()
    print(event,values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break



window.close()
