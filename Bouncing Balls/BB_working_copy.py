# Bu kod çarpışan topları sektirmeye ve renklerini değiştirmeye çalışıyor. Geliştirelebilir.

from tkinter import *
import time
import random
from math import *

"""
Group Name: METUROAM

Mehmet Baran Erol, 2307577
Mustafa Akbaba, 2306850
Emre Dağ, 2307361
Özgür Gülsuna, 2307668

"""
# try:

# Canvas width and height sizes.
width = 800
height = 600

color_main = "Red"

gui = Tk()

# Window size
gui.geometry("800x600")

gui.title("Meturoam Balls")
canvas = Canvas(gui, width=width, height=height, bg="white")
canvas.pack()


# RGB

fsize=50
maxcount = 10
colors = ["Green", "Red", "Blue"]


def radius(x1, x2):
    return abs(x1 - x2) / 2


def distance(pos, pos2):
    center1_x = (pos[0] + pos[2]) / 2
    center1_y = (pos[1] + pos[3]) / 2
    center2_x = (pos2[0] + pos2[2]) / 2
    center2_y = (pos2[1] + pos2[3]) / 2
    return sqrt((center1_x - center2_x) ** 2 + (center1_y - center2_y) ** 2)

# Creating an array including random number of balls
balls = []

indexes = 0

# A class where balls are created with random colors and velocities at random locations
class Ballz:
    def __init__(
        self,
        x1=0,
        y1=0,
        x2=0,
        y2=0,
        velx=0,
        vely=0,
        size = fsize,
        clr="Red",
        c=canvas.create_oval(0, 0, 0, 0, fill="Red"),
    ):
        self.x1 = random.randint(100, 700)
        self.y1 = random.randint(100, 500)
        self.x2 = self.x1 + size
        self.y2 = self.y1 + size
        self.velx = random.randint(-10, 10)
        self.vely = random.randint(-10, 10)
        self.clr = random.choice(colors)
        self.can = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.clr)
        self.size = size
    
    def Divide_and_concur(ball):
        pos = canvas.coords(ball.can)
        #radi = radius(pos[0], pos[2])
        #print(ball.size)
        balls.append(Ballz(x1 = pos[0], y1 = pos[1], size=ball.size/1.414))
        

    def bouncingWalls(ball):
        pos = canvas.coords(ball.can)  # Balls' positions for every
        radi = radius(pos[0], pos[2])
        if ball.clr == "Blue":
            r = radius(pos[0], pos[2])
            if pos[0] > width - radi:
                ball.x1 = 0
                ball.x2 = 2 * r
                pos = canvas.coords(ball.can)
                canvas.coords(ball.can, ball.x1, pos[1], ball.x2, pos[3])

            elif pos[1] > height-radi:
                ball.y1 = 0
                ball.y2 = 2 * r
                pos = canvas.coords(ball.can)
                canvas.coords(ball.can, pos[0], ball.y1, pos[2], ball.y2)

            elif pos[2] < radi:
                ball.x2 = width
                ball.x1 = width - 2 * r
                pos = canvas.coords(ball.can)
                canvas.coords(ball.can, ball.x1, pos[1], ball.x2, pos[3])

            elif pos[3] < radi:
                ball.y2 = height
                ball.y1 = height - 2 * r
                pos = canvas.coords(ball.can)
                canvas.coords(ball.can, pos[0], ball.y1, pos[2], ball.y2)
        else:
            #while (pos[1] >= height) or pos[3] >= width  ):
                #canvas.move(ball.can, ball.velx, ball.vely)
            if pos[3] >= height:
                a=pos[3]
                ball.vely = -ball.vely  
                canvas.coords(ball.can, ball.x1, ball.y1-(a-height), ball.x2, ball.y2-(a-height))
            if pos[1] <= 0:
                ball.vely = -ball.vely                
              #  canvas.coords(ball.can, ball.x1, ball.y1-pos[1], ball.x2, ball.y2-pos[1])
                #ball.y2=ball.y2-pos[1]+2000
                #ball.y1=ball.y1-pos[1]+2000

            if pos[2] >= width :
                ball.velx = -ball.velx
              #  canvas.coords(ball.can, ball.x1-(pos[2]-width), ball.y1, ball.x2-(pos[2]-width), ball.y2)                
                #ball.x1=ball.x1-(pos[2]-width+2000)
                #ball.x2=ball.x2-(pos[2]-width+2000)

            if pos[0] <= 0:
                ball.velx = -ball.velx 
               # canvas.coords(ball.can, ball.x1-pos[0], ball.y1, ball.x2-pos[0], ball.y2)                
                #ball.x2=ball.x2-pos[0]+2000
                #ball.x1=ball.x1-pos[0]+2000

                                

    def collision(ball1, ball2):
        global indexes
        pos1 = canvas.coords(ball1.can)  # Balls' positions for every
        pos2 = canvas.coords(ball2.can)  # Balls' positions for every
        dist = distance(pos1, pos2)
        radius1 = radius(pos1[0], pos1[2])
        radius2 = radius(pos2[0], pos2[2])
        
        if 0.0* (radius1 + radius2) < dist < (radius1 + radius2)*1:
            
            ball1.velx,ball2.velx = ball2.velx, ball1.velx
            ball1.vely,ball2.vely = ball2.vely, ball1.vely
            
            while dist < (radius1 + radius2):
                canvas.move(balls[i].can, balls[i].velx, balls[i].vely)
                pos1 = canvas.coords(ball1.can)  # Balls' positions for every
                pos2 = canvas.coords(ball2.can)
                dist = distance(pos1, pos2)


            # changing the colors
            if ball1.clr == ball2.clr:
                # divide the balls
                if len(balls)<maxcount:
                    Ballz.Divide_and_concur(ball1)
                    canvas.coords(ball2.can, ball2.x1, ball2.y1, ball2.x1+ball2.size/1.414, ball2.y1+ball2.size/1.414)

                color_pop1 = colors.pop(colors.index(ball1.clr))
                ball1.clr = colors[0]
                ball2.clr = colors[1]
                colors.append(color_pop1)
                canvas.itemconfigure(ball1.can, fill=ball1.clr)
                canvas.itemconfigure(ball2.can, fill=ball2.clr)
            else:
                color_pop1 = colors.pop(colors.index(ball1.clr))
                color_pop2 = colors.pop(colors.index(ball2.clr))
                ball1.clr = colors[0]
                ball2.clr = colors[0]
                colors.append(color_pop1)
                colors.append(color_pop2)
                canvas.itemconfigure(ball1.can, fill=ball1.clr)
                canvas.itemconfigure(ball2.can, fill=ball2.clr)
    
            if radius1 < fsize/2 and radius2 < fsize/2 and len(balls)<maxcount:
                canvas.coords(ball1.can, ball1.x1, ball1.y1, ball1.x1+ball1.size*1.414, ball1.y1+ball1.size*1.414)
                i1 = balls.index(ball2)
                i2= i1
                #print(i1, i2) 
                if i2 != i1: 
                    indexes = i1

# How many balls can an array have?
for i in range(random.randint(4,10)):
    balls.append(Ballz())

while True:
    for i in range(len(balls)):
        Ballz.bouncingWalls(balls[i])
        for j in range(i, len(balls)):
            Ballz.collision(balls[i], balls[j])
        canvas.move(balls[i].can, balls[i].velx, balls[i].vely)  # Balls are moved
        
        if indexes != 0:
            balls.pop(indexes)
    #indexes.reverse()

    #for i in indexes:
        #print(i)
    #if indexes != 0:
    

    gui.update()  # Updating gui with an update() command for every time step
    time.sleep(0.025)  # Time to sleep xD

gui.mainloop()




