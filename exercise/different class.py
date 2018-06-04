class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name

s=Student('yang')
print(s)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

for n in Fib():
    print(n)
f=Fib()
print(f[3])

class test(object):

    def __init__(self):
        self.name = 'yang'

    def __getattr__(self, attr):
        if attr=='score':
            print('your score is:')
            return 60

    def __call__(self):
        print('My name is %s.' % self.name)

a=test()
a()
print(a.score)
