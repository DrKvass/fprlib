import scipy as sp
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import uncertainties as un
from uncertainties import ufloat
from uncertainties.umath import *
from decimal import *

def mprint(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    print()
    
#-----------
def cfit(func, x_data, y_data, s=None, p0=None):
    tl = len(x_data)
    if len(s) != len(set(s)):
        print("Varable name is duplicated!")
        pass
    
    for i in range(len(s)):
        s[i] = str(s[i]).replace(" ","")
        
    if s == None:
        s = []
    if tl != len(y_data):
        print("Data lists are not of equal length!")
        pass
    elif tl <= 2:
        print("Data lists do not contain enough data points!")
        pass
    
    def y_compile():
        global cfit_n
        global y_model_compile
        y_model_compile = ""
        y_model_compile = "x_model,"
        for i in cfit_n:
            if i != list(cfit_n)[-1]:
                y_model_compile += str(i + ",")
            else:
                y_model_compile += str(i)
        return y_model_compile

        
    globals()["cfit_n"] = dict()
    globals()["y_model_compile"] = ""
    globals()["cfit_list"] = []
    global cfit_n
    global y_model_compile
    x_data = np.asarray(x_data)
    y_data = np.asarray(y_data)

    par, cov = curve_fit((func), x_data, y_data, p0)
    if len(s) != len(par):
        for i in range(1,len(par)+1):
            s.append(i)
    
    for i in range(len(par)):
        globals()[f"fit_{s[i]}"] = float(par[i])
        cfit_n[f"fit_{s[i]}"] = float(par[i])
        cfit_list = float(par[i])



    x_model = np.linspace(min(x_data),max(x_data),100)
    y_model_compile = y_compile()
    y_model = eval( f"func("+ y_model_compile +")" )

    plt.plot(x_data, y_data, "o", label="data")
    plt.plot(x_model, y_model, "-", label="fit")
    plt.legend()
    print("\n-| Fit values |----------------------------------------\n" )
    for i in cfit_n:
        print(str(i) + " : "+ str(cfit_n[i]))
    print("\n-| Parameter standard deviation values |---------------\n" )
    m = np.sqrt(np.diag(cov))
    for i in range(len(m)):
        print(list(cfit_n.keys())[i] + " stdev (1 sigma) : " + str(m[i]))

    print("\n-| Graph |---------------------------------------------\n" )
    plt.show()
