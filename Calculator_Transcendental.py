import sys
from Tkinter import *
import math
import pdb
from sinh import *
from sinx import *
from cosx import *
from root_x import *
from f_xpowx import *
from tenpowx import *
from pix import *

#fumction to clear the screen
def clear():
    input.delete(0,END)
    return

root = Tk()
frame = Frame(root,borderwidth=15,relief="raised")
frame.pack()

root.title("Transcendental calculator")

num1= StringVar()

topframe =Frame(root,borderwidth=15,relief="raised")
topframe.pack(side = TOP)


#Conversion to radian (function)
def toRadian(degree):
    return degree*3.14159/180.0

#hyperbolic sine function
#Power Function
def power(p,val) :
    q = 1;
    for i in range (1,val):
        q= q * p;
    return q;
#Factorial Function
def factorial (x) :
    fact = 1;
    if x == 0 :
        return fact
    else :
        for i in range (1,x) :
            fact = fact * i;
    return fact
#SIne Function
def sine_series(x):
 if len(input.get())==0:
    clear()
    n = "Math Domain Error";
    show_result(n)     
 else: 
    i = 1
    j = 0
    n = 100
    sum = 0
    while i <= n:
        sum += ((pow(-1.0, j)*pow((toRadian(float(x))), i))/math.factorial(i))
        i += 2
        j += 1
    clear()
    show_result(sum)
    
                   
#except ValueError :
 #           print ("Invalid number")

#Cosine Function
def cos_series(x):
 if len(input.get()) == 0:
    clear()
    n = "Math Domain Error";
    show_result(n)
 else:
    i = 0
    j = 0
    n = 170
    sum = 0
    while i <= n:
        if (i == 1):
            sum += 1
        else:
            sum += ((pow(-1.0, j)*pow((toRadian(float(x))), i))/math.factorial(i))
        i += 2
        j += 1
    clear()
    sum = '{0:.4f}'.format(sum)
    show_result(sum)

#hyperbolic sin function
def hyper_sine_series(x):s
 if len(input.get())==0:
     clear()
     n = "Math Domain Error";
     show_result(n)     
 else:    
    i = 1
    j = 0
    sum = 0
    float(x)
    while i <= 100:
        sum += ((pow(1.0, j)*pow((toRadian(float(x))), i))/math.factorial(i))
        i += 2
        j += 1
    clear();
    show_result(sum)
  #else :
      #show_result('Error in iput')

#Under root x function
def root_x(n):
 if len(input.get()) == 0:
    clear()
    n = "Math Domain Error";
    show_result(n)
 else:
    n = float(n)
    if n < 0:
        clear()
        n = "Math Domain Error";
        show_result(n)
        x=''
    else:
        x = n
        x = float(x)
        y = 1
        while x > y:
           x = (x+y)/2
           y = n/x
        clear()
    show_result(x)

#X power of X function
def xpowx(x):
 if len(input.get()) == 0:
    clear()
    n = "Math Domain Error";
    show_result(n)
 else:
    x=float(x)
    l=[]
    l.append(x)
    if x == 0:
        return 0
    elif x >= 1:
        for n in xrange(int(x)-1):
            l[0] = l[0]*x
    elif x <= 1:
        for n in xrange(int(x)+1,0):
            l[0] = l[0]*x
    l[0] = x**x
    clear()
    show_result(l[0])
# 10 Power of X function
def ten_pow_x(x):
 if len(input.get()) == 0:
    clear()
    n = "Math Domain Error";
    show_result(n)
 else:
    x=float(x)
    l=[]
    l.append(x)
    if x == 0:
        return 0
    elif x >= 1:
        for n in xrange(int(x)-1):
            l[0] = l[0]*x
    elif x <= 1:
        for n in xrange(int(x)+1,0):
            l[0] = l[0]*x
    l[0] = 10**x
    clear()
    show_result(l[0])
    
# Pi power of X function
def pi_pow_x(x):
 if len(input.get()) == 0:
    clear()
    n = "Math Domain Error";
    show_result(n)
 else:
    x= int(x)
    output = 1
    for x in range (0,x):
          output = output * 3.14159
          output = float(output)
    clear()
    show_result(output)


def p_x(x):
 pdb.set_trace()
 if len(input.get()) == 0:
    clear()
    n = "Math Domain Error";
    show_result(n)
 else:
    z=3.1425871
    y = float(x)
    w = pow(z,y)
    clear()
    show_result(float(w))
    
input=Entry(root,textvariable = num1, bd=80, insertwidth=1)
input.pack(side = TOP ,ipady=10,ipadx=5)


def backspace(inputval):
 #   self.cancel()
     str = inputval.rfind(inputval[-1:])
     input.delete(str,END)
#Output Result Show function
def show_result(inputVal):
      input.insert(END,inputVal)

#User Interface Creation done here and below
frame1 = Frame(root,borderwidth=25,bd=80, relief="groove")
frame1.pack(side=TOP,ipadx=9)
button1 = Button(frame1,command=lambda: show_result("1"),padx=16, pady=16,bd=8, text="1",fg="black")
button1.pack(side=LEFT)
button2 = Button(frame1,command=lambda: show_result("2"),padx=16, pady=16, bd=8, text="2",fg="black")
button2.pack(side=LEFT)
button3 = Button(frame1,command=lambda: show_result("3"),padx=16, pady=16, bd=8, text="3",fg="black")
button3.pack(side=LEFT)
button4 = Button(frame1,command=clear ,padx=16, pady=16, bd=8, text="C",fg="black")
button4.pack(side=LEFT)
button5 = Button(frame1,command=lambda: ten_pow_x(input.get()),padx=16, pady=16, bd=8, text="10^X",fg="black")
button5.pack(side=LEFT)

frame2 = Frame(root,borderwidth=25,bd=80,relief="groove")
frame2.pack(side=TOP,ipadx=0,ipady=0)
button1 = Button(frame2,command=lambda: show_result("4") ,relief=GROOVE,padx=16, pady=16, bd=8, text="4",fg="black")
button1.pack(side=LEFT)
button2 = Button(frame2,command=lambda: show_result("5") ,padx=16, pady=16, bd=8, text="5",fg="black")
button2.pack(side=LEFT)
button3 = Button(frame2,command=lambda: show_result("6") ,padx=16, pady=16, bd=8, text="6",fg="black")
button3.pack(side=LEFT)
button4 = Button(frame2,command=lambda: sine_series(input.get()),padx=16, pady=16, bd=8, text="SinX",fg="black")
button4.pack(side=LEFT)
button5 = Button(frame2,command=lambda: cos_series(input.get()),padx=16, pady=16, bd=8, text="CosX",fg="black")
button5.pack(side=LEFT)

frame3 = Frame(root,borderwidth=25,bd=80,relief="groove")
frame3.pack(side=TOP,ipadx=4)
button1 = Button(frame3,command=lambda: show_result("7") ,padx=16, pady=16, bd=8, text="7",fg="black")
button1.pack(side=LEFT)
button2 = Button(frame3,command=lambda: show_result("8") ,padx=16, pady=16, bd=8, text="8",fg="black")
button2.pack(side=LEFT)
button3 = Button(frame3,command=lambda: show_result("9") ,padx=16, pady=16, bd=8, text="9",fg="black")
button3.pack(side=LEFT)
button4 = Button(frame3,command=lambda: root_x(input.get()),padx=16, pady=16, bd=8, text="\/X",fg="black")
button4.pack(side=LEFT)
button5 = Button(frame3,command=lambda: hyper_sine_series(input.get()),padx=16, pady=16, bd=8,text=" Sinh ",fg="black")
button5.pack(side=LEFT)

frame4 = Frame(root,borderwidth=25,bd=80,relief="groove")
frame4.pack(side=TOP,ipadx=0)
button1 = Button(frame4,command=lambda: show_result("0") ,padx=16, pady=16, bd=8, text="0",fg="black")
button1.pack(side=LEFT)
button1 = Button(frame4,command=lambda: show_result(".") ,padx=16, pady=16, bd=8, text=".",fg="black")
button1.pack(side=LEFT)
button2= Button(frame4,command=lambda: xpowx(input.get()),padx=16, pady=16, bd=8, text="X^x",fg="black")
button2.pack(side=LEFT)
button3 = Button(frame4,command=lambda: p_x(input.get()),padx=16, pady=16, bd=8, text="Pi^X",fg="black")
button3.pack(side=LEFT)
button4 = Button(frame4,command=lambda: backspace((input.get())),padx=16, pady=16, bd=8, text="<--",fg="black")
button4.pack(side=LEFT)



root.mainloop()
