import random


def count_calls ():
    global calls
    calls += 1
    return calls

def string_info (string):
    #global tuple_
    count_calls()
    tuple_ = []
    tuple_.extend([len(string), string.upper(), string.lower()])
    tuple_ = tuple(tuple_)
    return tuple_

def is_contains (sting, list_to_search):
    count_calls()
    list = list_to_search
    for i in range(len(list)):
        if sting.lower() == list[i].lower():
            answer = True
        else: answer = False
        return answer

calls = 0
count = int(input('Введите колличество слов на проверку: '))
for i in range(count):
    string = input('Введите строку: ')
    tuple_ = string_info(string)
    print(tuple_)
    answer = is_contains(string,['СТРОКА', 'строка', 'СтроКА', 'стр', 'СТРК'])
    print(answer)
print("Колличество выполнений функций: ", calls)