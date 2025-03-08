import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE = "Connecting dogs"

current_dog = 0
total_dog = 8
start_time = 0
total_time = 0
dogs = []
lines = []

def create_dog():
    global start_time
    for i in range(total_dog):
        dog = Actor("dog")
        dog.pos = randint(40,760), randint(40,560)
        dogs.append(dog)
    start_time = time()

def draw():
    global total_time
    screen.blit("bg",(0,0))
    num = 1
    for dog in dogs:
        screen.draw.text(str(num),(dog.pos[0],dog.pos[1] + 40))
        dog.draw()
        num = num + 1
        
def update():
    pass






create_dog()
pgzrun.go()