with open('C:/pythontest/test01.txt', 'r') as f:
    print(f.read(2))
    print(f.readline())

with open('C:/pythontest/test01.txt', 'a') as t:
    t.write(' see you next time')

with open('C:/pythontest/test01.txt', 'r') as n:
    print(n.read())