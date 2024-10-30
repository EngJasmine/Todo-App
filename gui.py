import FreeSimpleGUI as sg
# Define the layout
label=sg.Text('Type in a to-do')
input_box=sg.InputText(tooltip='Enter todo')
add_button=sg.Button('Add')
# Create the window
window = sg.Window("My To-Do Application", [[label],[input_box,add_button]])
# Event Loop
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
  elif event == "Add":
    print("Button clicked!")
window.close()