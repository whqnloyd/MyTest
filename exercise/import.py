class student():
    def __init__(self,score):
        self.score=score

from testclass import set_score

a=student
set_score(a,40)
print(a.score)