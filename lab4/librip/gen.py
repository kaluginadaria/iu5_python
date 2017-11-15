import random


# Генератор вычленения полей из массива словарей
# Пример:
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Диван для отдыха2', 'price2': 5300, 'color': 'black'}
 ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}


def get_data(item, key):
    try:
        res = item[key]
        return res
    except Exception:
        return None


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        key = args[0]
        for item in items:
            res = get_data(item, key)
            yield res
    else:
        for item in items:
            res = { key:get_data(item, key) for key in args }
            yield res


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in range(num_count):
        res = random.randint(begin, end)
        yield res




