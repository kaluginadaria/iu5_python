# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2

import functools

def print_result_helper(func, res):
    print(func.__name__)
    tp = type(res).__name__
    if tp == 'list':
        [print(i) for i in res]
    elif tp == 'dict':
        [print('{0}={1}'.format(k,v)) for k,v in res.items()]
    else:
        print(res)


def print_result(func):
    @functools.wraps(func)
    def decorated_func(*args, **kwargs):
        res = func(*args, **kwargs)
        print_result_helper(func, res)
        return res
    return decorated_func