from enum import Enum,unique

month=Enum('month',( 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'dep', 'dct', 'nov', 'dec'))

for name, member in month.__members__.items():
    print(name, member, member.value)

@unique
class weekday(Enum):
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6
print(weekday.thu.value)
