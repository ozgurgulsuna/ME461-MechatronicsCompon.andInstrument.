from tkinter import *
import time
import random

gui = Tk()
gui.geometry("1000x1000")
gui.title("Red Ball Bouncing")
canvas = Canvas(gui, width=1000,height=1000,bg='white')
canvas.pack()

colors = ["Green","Red","Blue"]


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
        




balls = []
n = random.randint(10,25)

for i in range(n):
    balls.append(Ballz())

    
        
        
        

'''
ball1 = canvas.create_oval(5,5,60,60, fill='red')
ball2 = canvas.create_oval(150,150,200,200, fill='blue')


xa = 5
ya = 10
'''





while True:
    for i in range(len(balls)):
        canvas.move(balls[i].can,balls[i].velx,balls[i].vely)
        pos=canvas.coords(balls[i].can)
        if pos[3] >=1000 or pos[1] <=0:
            balls[i].vely = -balls[i].vely
        if pos[2] >=1000 or pos[0] <=0:
            balls[i].velx = -balls[i].velx
            
            
    gui.update()
    time.sleep(.025)

gui.mainloop()

