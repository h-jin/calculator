
import sys
from Tkinter import *
import math
import pdb
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