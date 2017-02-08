from grid import *
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

def add():
    string = E1.get()
    charList = []
    for char in string:
        if "0" <= char <= "9":
                char = int(char)
                charList.append(char)
        elif char == "-":
                charList.append(char)

    for i in range(len(charList)):
            
            if charList[i] == "-":
                    charList[i+1] = -charList[i+1]
                    charList.remove(charList[i])

    vector_1 = Vector(charList[0],charList[1])
    vector_2 = Vector(charList[2],charList[3])

    E1.insert(vector_1 + vector_2)

clear_button.pack(side = BOTTOM)
add_button = Button(master=root, text="Add", command=add)
add_button.pack(side = BOTTOM)

w = World(10,10)
a = Vector(1,1)
a.drawVector()

mainloop()
