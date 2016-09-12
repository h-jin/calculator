import sys
from Tkinter import *
import math
import pdb
import Calculator_Transcendental

def hyper_sine_series(x):
 print x
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
