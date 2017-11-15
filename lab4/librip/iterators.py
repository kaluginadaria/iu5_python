import itertools

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        #self.items = items
        self.items = iter(items) if isinstance(items, list) else items
        self.ignore_case = False
        #self.current = 0
        self.duplicates = []
        self.ignore_case = kwargs.get('ignore_case', False)
        #for k, v in kwargs.items():
        #    if k == 'ignore_case' and v == True:
        #        self.ignore_case = True

        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False


    def __next2__(self):
        try:
            cur = self.items[self.current]
            self.current += 1
            return cur
        except Exception:
            raise StopIteration


    def __next__(self):
        while True:
            try:

                #if isinstance(self.items, list):
                #    cur = self.items[self.current]
                #    self.current += 1
                #else:
                #    cur = next(self.items)

                cur = next(self.items)

                if isinstance(cur, str) and self.ignore_case is True:
                    cur_check = cur.upper()
                else:
                    cur_check = cur

                if not cur_check in self.duplicates:
                    self.duplicates.append(cur_check)
                    return cur
            except Exception:
                raise StopIteration


    def __iter__(self):
        return self
