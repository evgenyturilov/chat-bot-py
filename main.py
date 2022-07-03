# Простейший чат-бот, работающий по схеме
# {Вопрос на входе} => {Алгоритм ответа} => {Ответ на выходе}


import random
import re
import nltk

#text = input()
#if text in ['Привет', 'Здорово', 'Хэллоу']:
#    print(random.choice(['Здрасте', 'Йоу', 'Приветики']))
#elif text in ['Пока', 'Увидимся', 'Чао']:
#    print(random.choice(['До встречи', 'Бай-бай!', 'Чао!']))
#else:
#    print('Не понял...')

# Для очистки текста будем использовать:
#   1. функцию lower() для приведения к нижнему регистру
#   2. регулярные выражения (RegExp/ Регэкспы) для очистки текста от знаков препитания библиотека re
#   3. функцию find() для удаления лишних слов
#   4. библиотеку levenstein для фильтра опечаток import nltk 'nltk.org'

# Функция очищения текста
# "Привет!!!" -> "привет"
def filter(text):
    text = text.lower()
    expression = r'[^\w\s]' # Регулярное выражение = "Все, что не слово и не пробел"
    return re.sub(expression, '', text) # substitute - заменить все что не слово и не пробел на ""

# Функция проверки правильности пользовательского ввода

def text_match(user_text, example):
    user_text = filter(user_text)
    example = filter(example)
    # Фраза содержится в другой
    if user_text.find(example) != -1: # Если example найден внутри user_text
        return True
    if example.find(user_text) != -1: # Если user_text найден внутри example
        return True


    example_length = len(example) # Длина фразы example
    # Если фраза содержится в другой, то нужно определить на сколько они отличаются, т.е. проверить на опечатки
    # На сколько (%) отличаются фразы
    difference = nltk.edit_distance(user_text, example)/example_length

    return difference < 0.4 # возвращает значение


# База данных вопросов и ответов -> организация фраз по намерениям

# Определение намерений пользователя
# {Вопрос на входе} => {Алгоритм ответа} => {Ответ на выходе}
# {Примеры вопросов} => {Выбирался нужный вопрос с помощью text_match} => {Выдать вариант ответа}
# Интент - намерения пользователя = зачем он это спросил?
INTENTS = {
    'hello': {
        'examples': ['Привет', 'Хэллоу', 'Хай'],
        'response': ['Здрасте', 'Йоу', 'Салют'],
    },
    'how-are-you': {
        'examples': ['Как дела', 'Чем занят', 'Чо по чем'],
        'response': ['Вроде ничего', 'На чиле, на расслабоне', 'Так себе'],
    },
}
# в INTENTS мы можем записывать сколько угодно фраз
# или поместить в файл или БД

# Определить намерение по тексту
# "Чем занят" => "how-are-you"

def get_intent(text):
    # Проверить все существующие INTENTS
    for intent_name in INTENTS.keys():
        examples = INTENTS[intent_name]['examples']  
    # Какой-нибудь один будет иметь example  похожий на text
    # Проверяем все examples 
        for example in examples:
            if text_match(text, example):
                return intent_name

    

# Берет случайный response для данного intent
def get_response(intent):
    return random.choice(INTENTS[intent]['response'])


def bot(text):
    intent = get_intent(text)       # Найти намерение
    if not intent:                  # Если намерение не найдено
        print('Ничего не понятно')
    else:                           # Если намерение найдено
        print(get_response(intent))

text = ''
while text != 'Выход':
    text = input()
    bot(text)



