import telebot
import random

token = "7348773063:AAEM-Nmfy8yNnrQfPO_rPvV-VDYeDnJgTdQ"


HELP = """
/help - напечатать справку о программе
/add - добавить задачу в список (имя задачи будет запрашиваться)
/show - напечатать все добавленные задачи
/random - добавляет произвольную задачу на дату Сегодня
"""

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

bot = telebot.TeleBot(token)

tasks={ }

my_name="Антон"

def add_todo(date, task):
    if date in tasks:
        #Дата есть в словаре
        #Добавляем в список задачу
        tasks[date].append(task)
    else:
        #Даты в словаре нет
        #Создаем запись с ключом date
        tasks[date]=[]
        tasks[date].append(task)



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['random'])
def random_add(message):
    randomtask = random.choice(RANDOM_TASKS)
    randomdate = "сегодня"
    add_todo(randomdate, randomtask)
    bot.send_message(message.chat.id, "Произвольная задача добавлена!!!")


@bot.message_handler(commands=['add'])
def add(message):
    print(message.text)
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    if len(task)>3:
        add_todo(date, task)
        bot.send_message(message.chat.id, "Команда принята")
        bot.send_message(message.chat.id, f"Задача {task} добавлена на дату {date}")
    else:
        bot.send_message(message.chat.id, f"Задача {task} некорретна. Недостаточное описание")

@bot.message_handler(commands=['show', 'print'])
def show(message):
    for str in tasks:
        text=""
        count = 1
        #bot.send_message(message.chat.id, str)
        for i in tasks[str]:
            text = text + "[]" + " - "+ i + "\n"
          # bot.send_message(message.chat.id, f"{count}- {i}")
            count+=1
        bot.send_message(message.chat.id, str.upper() + "\n" + text)


@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        text="Ба! Знакомые все лица!"
    else:
        text=message.text
    bot.send_message(message.chat.id, text)


bot.polling()
