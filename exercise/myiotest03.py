import os
print(os.name)
print(os.environ)
print(os.environ.get('PATH'))

os.path.abspath('.')
os.path.join('C:/test fldor', 'testdir')

os.rename('C:/test fldor/test.txt', 'test.py')
os.remove('test.py')

[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

def findFile(str, path='.'):
    for f in os.listdir(path):
        fPath = os.path.join(path, f)
        if os.path.isfile(fPath) and str in f:
            print(fPath)
        if os.path.isdir(fPath):
            findFile(str, fPath)