import sys
from Tkinter import *
import math
import pdb
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