from tkinter import *
import tkinter as tk

pencere = tk.Tk()
pencere.geometry("360x480")
pencere.title("Hesap Makinesi")

def button(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 
 
def equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
    
def fact():
    fakt = math.factorial(int(self.entry.get()))
    input_text.set(fakt)       
 
expression = ""

    
input_text = StringVar()
main = tk.Entry(pencere, textvariable=input_text)
main.place(x=90, y=50)

button1 = tk.Button(pencere, text=' 1 ', command=lambda: button(1)) 
button1.place(x= 100, y =110) 
 
button2 = tk.Button(pencere, text=' 2 ', command=lambda: button(2)) 
button2.place(x= 130, y =110) 
 
button3 = tk.Button(pencere, text=' 3 ', command=lambda: button(3)) 
button3.place(x= 160, y =110) 
 
button4 = tk.Button(pencere, text=' 4 ', command=lambda: button(4)) 
button4.place(x= 100, y =150) 
 
button5 = tk.Button(pencere, text=' 5 ', command=lambda: button(5)) 
button5.place(x= 130, y =150) 
 
button6 = tk.Button(pencere, text=' 6 ', command=lambda: button(6)) 
button6.place(x= 160, y =150) 
 
button7 = tk.Button(pencere, text=' 7 ', command=lambda: button(7)) 
button7.place(x= 100, y =190) 
 
button8 = tk.Button(pencere, text=' 8 ', command=lambda: button(8)) 
button8.place(x= 130, y =190) 
 
button9 = tk.Button(pencere, text=' 9 ', command=lambda: button(9)) 
button9.place(x= 160, y =190) 
 
button0 = tk.Button(pencere, text=' 0 ', command=lambda: button(0)) 
button0.place(x= 130, y = 230) 

top = tk.Button(pencere, text="+", command=lambda: button("+"))
top.place(x=230, y=110)
cık = tk.Button(pencere, text="-", command=lambda: button("-"))
cık.place(x=230, y=150)
carp = tk.Button(pencere, text="*", command=lambda: button("*"))
carp.place(x=230, y=190)
bol = tk.Button(pencere, text="/", command=lambda: button("/"))
bol.place(x=230, y=230)
clear = tk.Button(pencere, text="C", command =lambda: clear)
clear.place(x= 260, y= 110)
eq = tk.Button(pencere, text="=", command=lambda: equal())
eq.place(x= 260, y= 150)
fakt = tk.Button(pencere, text="!",command=lambda: fact)
fakt.place(x=260, y=190)



pencere.mainloop()

