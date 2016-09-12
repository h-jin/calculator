import sys
from Tkinter import *
import math
import pdb
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