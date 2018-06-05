import sqlite3

print('creating connection...')
conn = sqlite3.connect('data/test.db')
print('creating cursor...')
cursor = conn.cursor()
#print('creating form...')
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#print('inserting record...')
#cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
cursor.execute('select * from user where id=?', ('1',))
z = cursor.fetchall()
#rowcount 返回执行结果，影响的行数
#x = cursor.rowcount
#print('the id is:',x)
print('the content is:',z)
print('closing cursor...')
cursor.close()
print('commit...')
conn.commit()
print('closing connection')
conn.close()
