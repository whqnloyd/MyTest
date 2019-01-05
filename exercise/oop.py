class Animal(object):
    def __init__(self,
                 name,
                 size):
        self.name = name
        self.size = size

    def run(self):
        print('animal is running...')

    def print_properties(self):
        print('%s,%s'%(self.name,self.size))

class Dog(Animal):
    def run(self):
        print('dog is running...')
    def sound(self):
        print('wang wang!')

class Cat(Animal):
    def sound(self):
        print('miao miao!')

def run(object):
    object.run()

dog = Dog('mike',20)
cat = Cat('miky',5)

dog.isgood = 'good'
dog.print_properties()
print(dir(dog))
dog.sound()
dog.run()
run(dog)