import pickle
d = dict(name='Bob', age=20, score=88)

with open('C:/pythontest/write.txt','wb') as f:
    pickle.dump(d,f)

with open('C:/pythontest/write.txt','rb') as f:
    a=pickle.load(f)

print(a)