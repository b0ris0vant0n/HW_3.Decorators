from decors import logger, logger_2
import requests
from datetime import datetime

# 1) Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
@logger
def summator(a, b):
    return a + b
summator(4, 5)

# 2) Написать декоратор из п.1, но с параметром – путь к логам.
@logger_2(parameter='log2.txt')
def summator(a, b):
    return a + b
summator(4, 5)

# 3) Применить написанный логгер к приложению из любого предыдущего д/з.
@logger
def old_homework():
    result = []
    fromdate = str(int(datetime.timestamp((datetime(2022, 8, 10)))))
    todate = str(int(datetime.timestamp(datetime.now())))
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': fromdate, 'todate' : todate, 'order' : 'desc', 'sort' : 'activity' ,
              'filter' : 'default', 'site' : 'stackoverflow', 'tagged' : 'java'}
    response = requests.get(url, params=params)
    for item in response.json()['items']:
         result.append(f'{item["title"]}')
    return result

old_homework()