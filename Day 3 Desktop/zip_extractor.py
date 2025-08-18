import FreeSimpleGUI as sg
from zip_extractor_functions import extract_archive

sg.theme("Black")

label1 = sg.Text("Select an Archive")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="archive")

label2 = sg.Text("Select an Folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="Green")

window = sg.Window("Archive Extractor",
                   layout=[[label1,input1,choose_button1],
                   [label2,input2,choose_button2],
                   [extract_button,output_label]])
while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break

    if event == "Extract":
        archive_path = values['archive']
        dest_folder = values['folder']

        if archive_path and dest_folder:
            extract_archive(archive_path, dest_folder)
            window["output"].update(value="Extraction Completed")
        else:
            sg.popup("Please select an archive file and a destination folder.")

window.close()