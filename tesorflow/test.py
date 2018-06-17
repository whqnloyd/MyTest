replace = [1.0] * 3
sum = []
'''
with open('data/test.txt', 'r') as f:
    for temp in f.readlines():
        temp1 = temp.split('\t')
        temp1.extend(replace)
        temp1 = list(map(float, temp1))
        sum.append(temp1)
print(sum)
'''

with open('data/test.txt', 'r') as f:
    for i in range(2):
        temp = f.readline()
        temp1 = temp.split('\t')
        temp1 = list(map(float, temp1))
        temp1.extend(replace)
        sum.append(temp1)
print(sum)
