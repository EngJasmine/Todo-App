from multiprocessing.managers import Value

import FreeSimpleGUI as sg
from FreeSimpleGUI import InputText

from functions import get_todos,write_todos


# Define the layout
label=sg.Text('Type in a to-do')
input_box=sg.InputText(tooltip='Enter todo',key='todo')
add_button=sg.Button('Add')
list_box=sg.Listbox(values=get_todos(),
                    key='todos',
                    enable_events=True,
                    size=[45,10])
edit_button=sg.Button('Edit')

# Create the window
window = sg.Window("My To-Do Application",
                   [[label],[input_box,add_button],[list_box,edit_button]],
                   font=('Helvetica', 20))
# Event Loop
while True:
  event, values = window.read()

  match event:

    case sg.WIN_CLOSED:
      break
    case "Add":

      todos=get_todos()
      newTodo=values['todo'] + '\n'
      todos.append(newTodo)
      write_todos(todos)
      window['todos'].update(values=todos)
      window['todo'].update(value=' ')
    case'Edit':

      todo_to_edit=values['todos'][0]
      new_user_todo=values['todo'] + '\n'
      todos=get_todos()
      index=todos.index(todo_to_edit)
      todos[index]=new_user_todo
      write_todos(todos)
      window['todos'].update(values=todos)
    case 'todos':
      window['todo'].update(value=values['todos'][0])




window.close()