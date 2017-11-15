#!/usr/bin/env python3

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
#res = sorted([(lambda k : abs(k))(i) for i in data])

res = sorted(data, key=lambda x: abs(x))
print(res)

