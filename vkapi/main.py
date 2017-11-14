import friends
import getid
import datetime
import matplotlib.pyplot as plt

name = input()
today = datetime.datetime.today()
id = getid.GetId()

uid= id.execute(name)

frnd = friends.Friends()

frnd = frnd.execute(uid)
a = []
for i in frnd:
    if 'bdate' not in i:
        continue
    if len(i['bdate']) > 5:

        d = datetime.datetime.strptime(i['bdate'], "%d.%m.%Y")
        y = int((str((today - d) / 365)[0:2]))

        a.append(y)

plt.hist(
    a,
    40
)
plt.show()
