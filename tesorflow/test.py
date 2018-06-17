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


def train_batch_x(f, num):
    sum = []
    for i in range(num):
        temp = f.readline()
        temp1 = temp.split('\t')
        temp1 = list(map(float, temp1))
        sum.append(temp1)
    return sum

with open('data/test.txt', 'r') as f:
    text = []
    for i in range(3):
        batch_size = 1
        x = train_batch_x(f, batch_size)
        text.append(x)
print(text)
