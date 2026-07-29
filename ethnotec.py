'''class Animal:
    def eat(self):
        print("Animal eats food")

class Bird:
    def fly(self):
        print("Bird can fly")

class Parrot(Animal, Bird):
    def speak(self):
        print("Parrot can speak")

p = Parrot()

p.eat()
p.fly()
p.speak()'''

'''class photo:
    def take_photo(self):
        print("taking photo")
class playing(photo):
    def playing_game(self):
        print("playing game")
class Calling(playing):
    def make_call(self):
        print("Calling")
c = Calling()
c.take_photo()
c.playing_game()
c.make_call()'''

'''class name:
    def show_name(self):
        print("name")
class Age(name):
    def show_age(self):
        print("age")
class salary(Age):
    def show_salary(self):
        print("salary")
c=salary()
c. show_name()
c.show_age()
c.show_salary()'''

'''class Animal:
    def sound(self):
        print("animal makes sounds ")
class dog(Animal):
    def sound(self):
        print("braks")
class cat(Animal):
    def sound(self):
        print("meow")
d=dog()
c=cat()
d.sound()
c.sound()'''

'''class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
r = rectangle(10,5)
r.area()'''

'''class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,r):
        self.r=r
       
    def area(self):
        print(3.14*self.r*self.r)
c=circle(3)
c.area() '''

import modules

print(modules.add(10,20))
print(modules.mul(10,20))  
print(modules.divide(10, 20))  
print(modules.flordivision(10, 20))