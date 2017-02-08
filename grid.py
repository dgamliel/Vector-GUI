import cTurtle
import math
import random

class World:
    def __init__(self, NX, NY):
        self.NX = NX
        self.NY = NY
        self.wturtle = cTurtle.Turtle()
        self.drawInit()  # draw world grid
        self.grid = []  # list of lists grid positions
        for j in range(NY):
            self.grid.append([])
            for i in range(NX):
                self.grid[j].append(None)
            

    def drawInit(self):
        # setup world grid
        self.wturtle.speed(0)
        self.wturtle.ht()
        self.wturtle.setWorldCoordinates(-0.1*self.NX, -0.1*self.NY, 1.1*self.NX, 1.1*self.NY)
        for i in range(self.NX + 1):
            self.wturtle.up()
            self.wturtle.goto(i, 0)
            self.wturtle.down()
            self.wturtle.goto(i, self.NY)
        for j in range(self.NY + 1):
            self.wturtle.up()
            self.wturtle.goto(0, j)
            self.wturtle.down()
            self.wturtle.goto(self.NX, j)
            
    def freezeScreen(self):
        self.wturtle.exitOnClick()

class Vector(World):
        
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        v1 = self.get()
        v2 = other.get()

        
        self.x = v2[0]+v1[0]
        self.y = v2[1]+v1[1]
        if self.z!=None:
            self.z = v2[2]+v1[2]
            addTup = (self.x,self.y,self.z)
        else:
            addTup = (self.x,self.y)
        return addTup

    def get(self):

        return (self.x, self.y, self.z)

    def __sub__(self, other): #subtracts components of vector
        v1 = self.get()
        v2 = other.get()

        
        self.x = v1[0]-v2[0]
        self.y = v1[1]-v2[1]
        self.z = v1[2]-v2[2]
        
        return (self.x, self.y, self.z)

    def __mul__(self, other): #dot product
        v1 = self.get()
        v2 = other.get()

        
        self.x = v2[0]*v1[0]
        self.y = v2[1]*v1[1]
        self.z = v2[2]*v1[2]
        
        return self.x + self.y + self.z

    def drawVector(self): #places turtle at origin and draws vector
        self.wturtle.up()
        self.wturtle.goto(self.NX/2, self.NY/2)
        self.wturtle.down()
        self.wturtle.goto(i + self.get[0],j+self.get[1])
        




