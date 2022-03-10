#Bu kod çarpışan topları sektirmeye ve renklerini değiştirmeye çalışıyor. Geliştirelebilir.

from tkinter import *
import time
import random
from math import *

'''
Group Name: METUROAM

Mehmet Baran Erol, 2307577
Mustafa Akbaba, 2306850
Emre Dağ, 2307361
Özgür Gülsuna, 2307668

'''
#try:
  
# Canvas width and height sizes.
width=800
height=600

color_main = 'Red'

gui = Tk()

# Window size
gui.geometry("800x600")

gui.title("Meturoam Balls")
canvas = Canvas(gui, width=width,height=height,bg='white')
canvas.pack()


# RGB
colors = ["Green","Red","Blue"]
def radius(x1,x2):
   return abs(x1-x2)/2
def distance(x1,y1,x2,y2,x3,y3,x4,y4):
   center1_x = (x1+x2)/2
   center1_y = (y1+y2)/2
   center2_x = (x3+x4)/2
   center2_y = (y3 + y4) / 2
   return sqrt((center1_x-center2_x)**2+(center1_y-center2_y)**2)

# A class where balls are created with random colors and velocities at random locations
class Ballz:

   def __init__(self,x1=0,y1=0,x2=0,y2=0,velx=0,vely=0,clr="Red",c = canvas.create_oval(0,0,0,0,fill = 'Red')):

       self.x1 = random.randint(100,700)
       self.y1 = random.randint(100,500)
       self.x2 = self.x1 + 50
       self.y2 = self.y1 + 50
       self.velx = random.randint(5,15)
       self.vely = random.randint(5,16)
       self.clr = random.choice(colors)
       self.can = canvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill = self.clr)


def collision(x_1, y_1, x_2, y_2, velx_1, vely_1, velx_2, vely_2, radius1, radius2, dist, clr1, clr2, ball1_can, ball2_can, pos_1, pos_2):
   # avoiding collision

   if 0.2 * (radius1+radius2) < dist < (radius1+radius2):
       if velx_1 * velx_2 < 0:
           velx_1 = -velx_1
           velx_2 = -velx_2
       if vely_1 * vely_2 < 0:
           vely_1 = -vely_1
           vely_2 = -vely_2


       #changing the colors
       if clr1 == clr2:
           color_pop1 = colors.pop(colors.index(clr1))
           clr1 = colors[0]
           clr2 = colors[1]
           colors.append(color_pop1)
           canvas.itemconfigure(ball1_can, fill=clr1)
           canvas.itemconfigure(ball2_can, fill=clr2)
       else:
           color_pop1 = colors.pop(colors.index(clr1))
           color_pop2 = colors.pop(colors.index(clr2))
           clr1 = colors[0]
           clr2 = colors[0]
           colors.append(color_pop1)
           colors.append(color_pop2)
           canvas.itemconfigure(ball1_can, fill=clr1)
           canvas.itemconfigure(ball2_can, fill=clr2)

       # divide the balls
       pos_1 = canvas.coords(ball1_can)
       pos_2 = canvas.coords(ball2_can)
       x_1 = pos_1[0] + 1
       y_1 = pos_1[1] + 1
       x_2 = pos_2[0] + 1
       y_2 = pos_2[1] + 1
       if x_1 - pos_1[2] == y_1 - pos_1[3] and x_2 - pos_2[2] == y_2 - pos_2[3]:
           canvas.coords(ball1_can, x_1, y_1, pos_1[2], pos_1[3])
           canvas.coords(ball2_can, x_2, y_2, pos_2[2], pos_2[3])

   return x_1, y_1, velx_1, vely_1, clr1, ball1_can, pos_1


# Creating an array including random number of balls
balls = []


# How many balls can an array have?
for i in range(random.randint(10,25)):
   balls.append(Ballz())



# Action of window is created using an infinite loop.
while True:
   for i in range(len(balls)):

       canvas.move(balls[i].can,balls[i].velx,balls[i].vely) # Balls are moved
       pos=canvas.coords(balls[i].can) # Balls' positions for every time interval
       for j in range(i, len(balls)):
           pos2 = canvas.coords(balls[j].can)
           balls[i].x1, balls[i].y1, balls[i].velx, balls[i].vely, balls[i].clr, balls[i].can, pos = \
               collision(balls[i].x1, balls[i].y1, balls[j].x1, balls[j].x2, balls[i].velx, balls[i].vely, balls[j].velx,
                                   balls[j].vely, radius(pos[0], pos[2]), radius(pos2[0], pos2[2]),
                                   distance(pos[0], pos[1], pos[2], pos[3], pos2[0], pos2[1], pos2[2],pos2[3]), balls[i].clr,
                                  balls[j].clr, balls[i].can, balls[j].can, pos, pos2)


       #Blue balls going through walls and coming the opposite walls
       if (balls[i].clr == 'Blue'):
           r=radius(pos[0], pos[2])
           if pos[0] > 800:
               balls[i].x1 = 0
               balls[i].x2 = 2*r
               pos = canvas.coords(balls[i].can)
               canvas.coords(balls[i].can, balls[i].x1, pos[1], balls[i].x2, pos[3])
           elif pos[1] > 600:
               balls[i].y1 = 0
               balls[i].y2 = 2*r
               pos = canvas.coords(balls[i].can)
               canvas.coords(balls[i].can, pos[0], balls[i].y1, pos[2], balls[i].y2)

           elif pos[2] < 0:
               balls[i].x2 = 800
               balls[i].x1 = 800-2*r
               pos = canvas.coords(balls[i].can)
               canvas.coords(balls[i].can, balls[i].x1, pos[1], balls[i].x2, pos[3])
           elif pos[3] < 0:
               balls[i].y2 = 600
               balls[i].y1 = 600-2*r
               pos = canvas.coords(balls[i].can)
               canvas.coords(balls[i].can, pos[0], balls[i].y1, pos[2], balls[i].y2)


       # Avoiding going through boundaries (walls)
       else:
           if pos[3] >= 600 or pos[1] <= 0:
               balls[i].vely = -balls[i].vely
           if pos[2] >= 800 or pos[0] <= 0:
               balls[i].velx = -balls[i].velx


   gui.update()       # Updating gui with an update() command for every time step
   time.sleep(.025)  # Time to sleep xD

gui.mainloop()
      

#except:
   #print("Hatasız kod olmaz!")

