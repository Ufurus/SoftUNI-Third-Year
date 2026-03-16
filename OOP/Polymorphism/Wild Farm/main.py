from project.animals.birds import Owl, Hen
from project.animals.mammals import *
from project.food import Meat, Vegetable, Fruit

hen = Tiger("Harry", 10, 'str')
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
