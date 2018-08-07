def evaluation():
    #evaluation
    grade = 0

    with open('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/text/L1.txt') as f:
        img_text = f.read()
    temp1 = img_text.replace(',', '')
    temp2 = temp1.replace('.', '')
    temp3 = temp2.strip()
    temp4 = temp3.replace('\n', '')
    temp = temp4.split(' ')
    with open('C:/Users/Luodai Yang/Projects/MyTest/qt test/open_img/text/speech.txt') as f:
        spch_text = f.read()
    user = spch_text.split(' ')

    if len(user) < (len(temp) + 3):
        for i in user:
            for ii in temp:
                if i == ii:
                    grade += 1
                    break
    else:
        print('speak too much')
        return 0

    grade = grade/len(temp)*100
    print('your grade is:', int(grade))
    return int(grade)


if __name__ == '__main__':
    a = evaluation()