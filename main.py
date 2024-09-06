HELP = '''
help - напечатать справку о программе
add - добавить задачу в список (имя задачи будет запрашиваться)
show - напечатать все добавленные задачи'''
tasks = []

command = input('Введите команду: ')
if command=='help':
    print(HELP)
elif command=='add':
    task = input('Введите название задания: ')
    tasks.append(task)
    print('Задача добавлена')
    print(tasks)
elif command=='show':
    print(tasks)
else:
    print('Неизвестная команда')