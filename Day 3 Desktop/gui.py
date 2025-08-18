from zip_creator import make_archive

import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")
# https://pypi.org/

clock = sg.Text("", key="clock")
label = sg.Text("Type a TODO")
input_box = sg.InputText(tooltip="Enter TODO", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos", enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My TODO Window',
                   layout=[
                           [clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',12))

while True:
    event, values = window.read(timeout=200)

    if event == sg.WIN_CLOSED:
        break

    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    #print(event, values)

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
            else:
                sg.popup("Please select an item to edit")

        case "todos":
            window['todo'].update(value=values['todos'][0].strip())

        case "Complete":
            if values['todos']:  # make sure something is selected
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            else:
                sg.popup("Please select an item to complete")

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break



window.close()
