class student():
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            print('score must be an integer!')
        if value < 0 or value > 100:
            print('score must between 0 ~ 100!')
        self._score = value

s=student()
s.score=60
print(s.score)
s.score=999
