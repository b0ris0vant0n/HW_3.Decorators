import datetime
import os

def logger(old_function):
    def new_function(*args, **kwargs):
        with open('log.txt', 'a') as file:
            result = old_function(*args, **kwargs)
            log = f'\n{datetime.datetime.now()} Вызвана функция {old_function.__name__} c аргументами {args} и {kwargs}, Результат = {result}'
            file.write(f'{log}')
            return result

    return new_function


def logger_2(parameter):
    BASE_PATH = os.getcwd()
    full_path = os.path.join(BASE_PATH, parameter)
    def decor(old_function):
        def new_function(*args, **kwargs):
            with open(full_path, 'a') as file:
                result = old_function(*args, **kwargs)
                log = f'\n{datetime.datetime.now()} Вызвана функция {old_function.__name__} c аргументами {args} и {kwargs}, Результат = {result}'
                file.write(f'{log}')
                return result

        return new_function
    return decor





