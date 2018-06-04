str = input('please input head string:')

with open ('output.txt','w') as tn:
    for line in open('input.txt','r') :
        if (line.find(str) >= 0):
            a = line.split('GN=')
            for s in a[1]:
                if (s == ' '):
                    break
                else:
                    tn.write(s)
                    print(s, end='')
            tn.write('\n')
            print('\n')
        else:
            tn.write('\n')
            print('\n')