filename = 'main.txt'


def read_data():
    with open(filename, 'r') as file:
        tasks = file.readlines()
        return tasks


def write_data(tasks):
    with open(filename, 'w') as file:
        file.writelines(tasks)

