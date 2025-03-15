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
        screen.draw.text(str(num),(dog.pos[0],dog.pos[1] + 35))
        dog.draw()
        num = num + 1
        
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    
    if current_dog < total_dog:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)
    
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)

def update():
    pass

def on_mouse_down(pos):
    global current_dog,lines
    if current_dog < total_dog:
        if dogs[current_dog].collidepoint(pos):
            if current_dog:
                lines.append(
                    (
                        dogs[current_dog-1].pos,
                        dogs[current_dog].pos
                    )
                )
            current_dog = current_dog + 1
        else:
            lines = []
            current_dog = 0






create_dog()
pgzrun.go()