class student(object):
    def set_age(self,age):
        self.age=age

def set_score(self,score):
    self.score=score
def get_score(self):
    return self.score

s=student()
from types import MethodType
s.update_score=MethodType(set_score,s)
s.show_score=MethodType(get_score,s)

s.name='yang'
s.set_age(25)
s.update_score(60)

print(s.show_score())
