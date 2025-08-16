import FreeSimpleGUI

import functions
import FreeSimpleGUI as sg

# https://pypi.org/

label = sg.Text("Type a TODO")
input_box = FreeSimpleGUI.InputText(tooltip="Enter TODO")
add_button = sg.Button("Add")

window = sg.Window('My TODO Window', layout=[[label], [input_box, add_button]])
window.read()
window.close()
