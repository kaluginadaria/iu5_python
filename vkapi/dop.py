new_lst = list(range(1,11))
print(new_lst)


#first

print([x**2 for x in new_lst])

#second

print(list(map(lambda x: x**2, new_lst)))