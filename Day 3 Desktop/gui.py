import FreeSimpleGUI

import functions
import FreeSimpleGUI as sg

# https://pypi.org/

label = sg.Text("Type a TODO")
input_box = FreeSimpleGUI.InputText(tooltip="Enter TODO", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos", enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window('My TODO Window',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica',12))

while True:
    event, values = window.read()
    print(event, values)

    match event:
        case "Add":
            new_todo = values['todo'].strip()
            if new_todo:
                todos = functions.get_todos()
                todos.append(new_todo + "\n")
                functions.write_todos(todos)
                window['todos'].update(values=todos)

        case "Edit":
            if values['todos']:  # make sure something is selected
                new_todo = values["todo"].strip()
                if new_todo:
                    todo_to_edit = values['todos'][0]
                    todos = functions.get_todos()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo + "\n"
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0].strip())

        case sg.WIN_CLOSED:
            break



window.close()
