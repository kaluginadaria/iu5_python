import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='dbuser',
    passwd='123',
    db='my_db'
)
db.set_character_set('utf8')
c = db.cursor()
c.execute('SET NAMES utf8;')
c.execute('SET CHARACTER SET utf8;')
c.execute('SET character_set_connection=utf8;')
c.execute("INSERT INTO orders (name, description) VALUES (%s, %s)", ('заказ 777', "какой то заказ 777"))

db.commit()

c.execute("SELECT * FROM orders")

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()
