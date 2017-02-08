from tkinter import *
from Vector import * 

root = Tk()

L1 = Label(root, text="Insert 2 Vectors to be added")
L1.pack(side = TOP)

E1 = Entry (bd=5)
E1.pack(side = LEFT, fill=X)

E1.insert(0, "")
def clear():
        E1.delete(0, END)
clear_button = Button(master=root, text="Clear", command=clear)
#creates array with vector value inputs
def getVectors():
    string = E1.get()
    charList = []
    #trims input to negative symbol and integer values only.
    for char in string:
        if "0" <= char <= "9":
                char = int(char)
                charList.append(char)
        elif char == "-":
                charList.append(char)
    #trims negative symbol and converts values to appropriate sign
    for i in range(len(charList)):
            if charList[i] == "-":
                    charList[i+1] = -charList[i+1]
                    charList.remove(charList[i])
    #checks if 3d or 2d vector
    if len(charList)>4:
            vector_1 = Vector(charList[0],charList[1],charList[2])
            vector_2 = Vector(charList[3],charList[4],charList[5])
    else:
            vector_1 = Vector(charList[0],charList[1])
            vector_2 = Vector(charList[2],charList[3])
    return (vector_1,vector_2)
def add():
    vectors = getVectors()
    print(vectors[0]+vectors[1])

def multiply():
    vectors = getVectors()
    print(vectors[0]*vectors[1])

def sub():
    vectors = getVectors()
    print(vectors[0]-vectors[1])

clear_button.pack(side = BOTTOM)
add_button = Button(master=root, text="  +  ", command=add)
add_button.pack(side = BOTTOM)
mul_button = Button(master=root, text="  x  ", command=multiply)
mul_button.pack(side = BOTTOM)
sub_button = Button(master=root, text="  -  ", command=sub)
sub_button.pack(side = BOTTOM)


mainloop()
