class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def set_score(self, score):
        self.__score = score

class freshman(Student):
    def __init__(self,name,score,gender):
        Student.__init__(self,name,score)
        self.gender=gender

class boyMxiIn():
    def run(self):
        print('running')

class girlMixIn():
    def smile(self):
        print('smiling')

class group1(freshman,boyMxiIn):
    pass

class group2(freshman,girlMixIn):
    pass

lisa =group2('Lisa', 99,'woman')
yang=group1('Yang',90,'man')
print(lisa.name, lisa.get_grade(),lisa.gender)
print(yang.name, yang.get_grade(),yang.gender)
yang.run()
lisa.set_score(60)
print(lisa.name,lisa.get_grade(),lisa.gender)
lisa.smile()
