'''
replace = [1.0] * 3
sum = []
'''

'''
with open('data/test.txt', 'r') as f:
    for temp in f.readlines():
        temp1 = temp.split('\t')
        temp1.extend(replace)
        temp1 = list(map(float, temp1))
        sum.append(temp1)
print(sum)
'''

'''
pin

def train_batch_x(f, num):
    sum = []
    
    for i in range(num):
        temp = f.readline()
        temp1 = temp.split('\t')
        temp1 = list(map(float, temp1))
        sum.append(temp1)
    pin = fd.tell()
    return sum

with open('data/test.txt', 'r') as f:
    text = []
    for i in range(3):
        batch_size = 1
        x = train_batch_x(f, batch_size)
        text.append(x)
print(text)
'''
text = []


def test_read():
    file = 'data/test.txt'
    with open(file, 'r') as fd:         # 获得一个句柄
        fd.seek(label, 0)
        for i in range(2):              # 读取三行数据
            text.append(fd.readline())
        label = fd.tell()
        print(label)
    print(text)


'''
# 再次阅读文件
with open(file, 'r') as f:           # 获得一个句柄
    f.seek(label, 0)           # 把文件读取指针移动到之前记录的位置
    text2 = f.readline()
print(text2)                    # 接着上次的位置继续向下读取
'''

