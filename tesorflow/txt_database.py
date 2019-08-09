class get_next_batch():

    def train_batch_x(num):
        sum = []
        with open('data/train_TCGA_x.txt', 'r') as f:
            for i in range(num):
                temp = f.readline()
                temp1 = temp.split('\t')
                temp1 = list(map(float, temp1))
                sum.append(temp1)
        return sum


    def train_batch_label(num):
        sum = []
        with open('data/train_TCGA_label.txt', 'r') as f:
            for i in range(num):
                temp = f.readline()
                temp1 = temp.split('\t')
                temp1 = list(map(float, temp1))
                sum.append(temp1)
        return sum


    def batch_x_test(num):
        sum = []
        with open('data/test_TCGA_x.txt', 'r') as f:
            for i in range(num):
                temp = f.readline()
                temp1 = temp.split('\t')
                temp1 = list(map(float, temp1))
                sum.append(temp1)
        return sum


    def batch_label_test(num):
        sum = []
        with open('data/test_TCGA_label.txt', 'r') as f:
            for i in range(num):
                temp = f.readline()
                temp1 = temp.split('\t')
                temp1 = list(map(float, temp1))
                sum.append(temp1)
        return sum