import sys
from Tkinter import *
import math
import pdb
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
