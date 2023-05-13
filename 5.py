import numpy as np
import matplotlib.pyplot as plt
import time

#funkce
f1 = lambda x: -6*x**3 + x**2 - 6
f2 = lambda x: 3*x -np.exp(4*x)
f3 = lambda x: 2*np.sin(-2*x+2)

#metoda biscekce
def metoda_b(f, a0, b0, delta = 1E-5):
    a, b = a0, b0
    x=0
    while b**2 - a **2 > 2*delta:
        x = (a + b)/2
        if f(a)*f(x) < 0:
            b = x
        else:
            a = x
    return x

#metoda newton
def metoda_n(f, a0, b0, delta = 1E-5):
    a, b = a0, b0
    def df(x, h = 1E-3):
        return (f(x+h)-f(x-h))/(2*h)
    xnew = (a+b)/2
    xold = a
    while abs(xnew - xold) > delta:
        xold = xnew
        xnew = xold - f(xold)/df(xold)
    return xnew

#závěr
def vysledek(f, a0, b0, x, title):
    print("Kořen funkce je: ", x)
    print("\n")
    start = time.time()
    plt.title(title)
    plt.plot(x, f(x), "bo")
    end = time.time()
    plt.plot(np.linspace(a0, b0, 100), f(np.linspace(a0, b0, 100)), "r")
    plt.show()
    print("\n")
    print(f"Čas: {str(end - start)} s")
    print("\n")

#Funkce 1
a1, b1 = -2, 1
funkce1="-6*x^3 + x^2 - 6"
vysledek(f=f1, a0 = a1, b0 = b1, x = metoda_b(f=f1, a0 = a1, b0 = b1), title="Půlení intervalů: " +funkce1)
print("\n")
vysledek(f=f1, a0 = a1, b0 = b1, x = metoda_n(f=f1, a0 = a1, b0 = b1), title="Newtonova metoda: " +funkce1)
print("\n")

#Funkce 2
a2, b2 = -1, 1
funkce2="3*x -e^(4*x)"
vysledek(f=f2, a0 = a2, b0 = b2, x = metoda_b(f=f2, a0 = a2, b0 = b2), title="Půlení intervalů: " +funkce2)
print("\n")
vysledek(f=f2, a0 = a2, b0 = b2, x = metoda_n(f=f2, a0 = a2, b0 = b2), title="Newtonova metoda: " +funkce2)
print("\n")

#Funkce 3
a3, b3 = -1, 2
funkce3="2*sin(-2*x+2)"
vysledek(f=f3, a0 = a3, b0 = b3, x = metoda_b(f=f3, a0 = a3, b0 = b3), title="Půlení intervalů: " +funkce3)
print("\n")
vysledek(f=f3, a0 = a3, b0 = b3, x = metoda_n(f=f3, a0 = a3, b0 = b3), title="Newtonova metoda: " +funkce3)
