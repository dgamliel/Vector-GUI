class Vector:
        
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

    def __sub__(self, other):
        v1 = self.get()
        v2 = other.get()
        self.x = v1[0]-v2[0]
        self.y = v1[1]-v2[1]
        if self.z!=None:
            self.z = v1[2]-v2[2]
            subTup = (self.x,self.y,self.z)
        else:
            subTup = (self.x,self.y)
        return subTup

    def __mul__(self, other):
        v1 = self.get()
        v2 = other.get()

        
        self.x = v2[0]*v1[0]
        self.y = v2[1]*v1[1]
        if self.z!=None:
            self.z = v2[2]*v1[2]
            multiple = self.x+self.y+self.z
        else:
            multiple = self.x+self.y
        return multiple
