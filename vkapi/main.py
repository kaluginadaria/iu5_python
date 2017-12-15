import friends
import getid
import datetime
import matplotlib.pyplot as plt
import random

name = input()
today = datetime.datetime.today()
id = getid.GetId()

uid= id.execute(name)

frnd = friends.Friends()

frnd = frnd.execute(uid)
a = []
random.seed(0)
some_dates = [random.randint(10,30) for x in range(10)]
print(some_dates)
for i in frnd:
    if 'bdate' not in i:
        continue
    if len(i['bdate']) > 5 :

        d = datetime.datetime.strptime(i['bdate'], "%d.%m.%Y")
        y = int((str((today - d) / 365)[0:2]))
        if y in some_dates:
            a.append(y)

plt.hist(
    a,
    40
)
plt.show()
#сгенерировать н друзей
#список чисел 1,10  2 способа
