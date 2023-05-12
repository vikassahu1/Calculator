# Calculator 
from tkinter import * 
import math

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = scvalue.get()
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                value = "Error"
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root = Tk()
root.geometry("400x450")
root.maxsize(400,450)
root.title("Calculator")
root.wm_iconbitmap("icon.ico")
root.config(background="black")

# Screen
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvariable=scvalue,font="lucida 40",relief=SUNKEN)
screen.pack(fill=X,padx=12,pady=12)

# Button
c=0
for i in range(2):
    f = Frame(root,pady=10,padx=10,bg="black")
    for j in range(4): 
        if c<10:
            b = Button(f, text=f"{c}", padx=20, pady=10, font="lucida 15 bold",bg="white",relief=SUNKEN)
            b.pack(side=LEFT, padx=5, pady=5)
            c+=1
            b.bind('<Button-1>', click)
            f.pack()

# Symbols 
f = Frame(root,pady=10,padx=10,bg="black")
b = Button(f, text=f"8", padx=20, pady=10, font="lucida 15 bold",bg="white",relief=SUNKEN)
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f, text=f"9", padx=20, pady=10, font="lucida 15 bold",bg="white",relief=SUNKEN)
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f, text=f"=", padx=14, pady=10, font="lucida 15 bold",bg="white",relief=SUNKEN)
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
b = Button(f, text=f"C", padx=20, pady=10, font="lucida 15 bold",bg="white",relief=SUNKEN)
b.pack(side=LEFT, padx=5, pady=5)
b.bind('<Button-1>', click)
f.pack()


f = Frame(root,pady=10,padx=10,bg="black")
arr1 = ["+","-","*","/"]
for i in arr1:
    b = Button(f, text=f"{i}", padx=20, pady=10, font="lucida 15 bold",bg="white",relief=SUNKEN)
    b.pack(side=LEFT, padx=5, pady=5)
    b.bind('<Button-1>', click)
    f.pack()


root.mainloop()