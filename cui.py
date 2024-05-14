from functions import read_data, write_data

while True:
    user_prompt = input("Enter add, delete, edit, show, or exit: ")
    user_prompt = user_prompt.strip()

    if user_prompt.startswith('add'):
        task = user_prompt[4:]
        tasks = read_data()
        tasks.append(task + "\n")
        write_data(tasks)

    elif user_prompt.startswith('show'):
        tasks = read_data()
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip('\n')}")

    elif user_prompt.startswith('exit'):
        break

    elif user_prompt.startswith('delete'):
        try:
            del_num = int(user_prompt[6:])
            tasks = read_data()
            tasks.pop(del_num - 1)
            write_data(tasks)

        except ValueError:
            print('please use the integer with delete command, Eg:- delete 2')
            continue

    elif user_prompt.startswith('edit'):
        try:
            edit_num = int(user_prompt[4:])
            tasks = read_data()
            index = edit_num - 1
            new_task = input(f"replace {tasks[index]} with: ")
            tasks[index] = new_task + '\n'
            write_data(tasks)

        except ValueError:
            print('please use the integer with edit command, Eg:- edit 2')
            continue

    else:
        print("Error: Please enter the right command")
        continue

