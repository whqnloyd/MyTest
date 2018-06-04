from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

t=StringIO('hello\nworld!')
while 1:
    str=t.readline()
    if str=='':
        break
    else :
        print(str.strip())