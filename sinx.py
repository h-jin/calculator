import sys
from Tkinter import *
import math
import pdb
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
    