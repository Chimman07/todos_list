import PySimpleGUI as kid
from functions import read_data, write_data
import os

if not os.path.exists("main.txt"):
    with open("main.txt", 'w') as file:
        pass

label1 = kid.Text('Enter the task to add in your list', background_color='black')
input_box1 = kid.InputText(tooltip='enter task', key='task')
add_button = kid.Button('Add')

data = kid.Listbox(enable_events=True, size=(45, 12), values=read_data(), key='tasks')

delete_button = kid.Button('Delete')
edit_button = kid.Button('Edit')
exit_button = kid.Button('Exit')
kid.theme('black')
window = kid.Window("My-Tasks-List", layout=[[label1], [input_box1, add_button], [data, edit_button],
                                             [delete_button], [exit_button]], )

while True:
    events, value = window.read()
    print(events)
    print(value)

    match events:
        case 'Add':
            tasks = read_data()
            new_task = value['task']
            tasks.append(new_task + '\n')
            write_data(tasks)
            window['tasks'].update(values=tasks)
            window['task'].update(value="")

        case 'Exit':
            break

        case kid.WIN_CLOSED:
            break

        case 'tasks':
            window['task'].update(value=value['tasks'][0])

        case 'Edit':
            try:
                tasks = read_data()
                index = tasks.index(value['tasks'][0])
                new_task = value['task']
                tasks[index] = new_task + '\n'
                write_data(tasks)
                window['tasks'].update(values=tasks)

            except IndexError or ValueError:
                message = ("you might have forgot to select the item \n"
                           "or may be you selected a single item multiple times")
                kid.popup_quick_message(message)
                continue

        case 'Delete':
            try:
                tasks = read_data()
                index = tasks.index(value['tasks'][0])
                tasks.pop(index)
                write_data(tasks)
                window['tasks'].update(values=tasks)
                window['task'].update(value="")

            except IndexError:
                kid.popup_quick_message('Select item to delete')
                continue

window.close()
