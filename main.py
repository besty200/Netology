import random

HELP = '''
help - напечатать справку о программе
add - добавить задачу в список (имя задачи будет запрашиваться)
show - напечатать все добавленные задачи
random - добавляет произвольную задачу на дату Сегодня'''
today=[]
tomorrow = []
other =[]

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

tasks = {

}

while True:
    commandos = input('Введите команду: ')
    if commandos=='help':
       print(HELP)
    elif commandos=='add':
       data = input('Введите дату:')
       task = input('Введите название задания: ')
       if data =='Сегодня':
           today.append(task)
           print('Задача добавлена')
       elif data =='Завтра':
           tomorrow.append(task)
           print('Задача добавлена')
       else:
           other.append(task)
           print('Задача добавлена')
    elif commandos=='show':
        print('Сегодня')
        print(today)
        print('Завтра')
        print(tomorrow)
        print('Другие')
        print(other)
    elif commandos=='random':
        task = random.choice(RANDOM_TASKS)
        today.append(task)
    elif commandos=='exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
       print('Неизвестная команда')
       break
