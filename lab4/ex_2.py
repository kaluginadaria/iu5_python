#!/usr/bin/env python3
from librip.gen import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2
print([x for x in Unique(data1)])
print([x for x in Unique(data2)])
print([x for x in Unique(['A','a','B','b'])])
print([x for x in Unique(['A','a','B','b'], ignore_case = True)])