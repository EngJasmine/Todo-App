from functions import get_todos,write_todos
import time

print(time.strftime(f'The time is %b-%d-%Y %H:%M:%S '))
while True:
    user_action=input('Type add, show, complete, edit, or exit :')
    user_action=user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo +'\n' )
        write_todos(todos)


    elif user_action.startswith('show'):
        todos = get_todos()
        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index+1}-{item}'
            print(row)


    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number-1
            todos = get_todos()
            new_todo = input('Enter the new todo :')
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print('Your command is not valued')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1
            todos = get_todos()
            todo_to_remove=todos[number].strip('\n')
            todos.pop(number)
            write_todos(todos)
            print(f'Todo {todo_to_remove} was removed from the list')
        except IndexError:
            print('The number you entered is not in the list !')
            continue
        except ValueError:
            print('Your command is not valued')
            continue


    elif user_action.startswith('exit'):
            break
    else:
        print('Please choose action from the list')
print('Bye')
