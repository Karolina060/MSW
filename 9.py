import numpy as np
import scipy.integrate

#Funkce
def f1(x):
    return -6*x**3 + x**2 - 6
def f2(x):
    return 3*x -np.exp(4*x)
def f3(x):
    return 2*np.sin(-2*x+2)

a = 0
b = 4
dx = 0.2

#Řešení
#analitické
def analytic(f, a, b):
    x = scipy.integrate.quad(f, a, b)
    return(x[0])

#trapeziodické
def trapeziod(f, a, b, dx):
    x = np.arange(a, b+dx, dx)
    y = f(x)
    return(scipy.integrate.simpson(y, x))

#simpsonovo
def simpson(f, a, b, dx):
    x = np.arange(a, b+dx, dx)
    y = f(x)
    return(scipy.integrate.simpson(y, x))

#rombergovo
def romberg(f, a, b):
    return(scipy.integrate.romberg(f, a, b))

#riemannuv čtverec
def rieman(f, a, b):
    return(scipy.integrate.quadrature(f, a, b)[0])

#Funkce 1
print("Funkce: -6*x^3 + x^2 - 6")
a1 = analytic(f1, a, b)
fu1 = trapeziod(f1, a, b, dx)
fu2 = romberg(f1, a, b)
fu3 = simpson(f1, a, b, dx)
fu4 = rieman(f1, a, b)
print(f"TRAPEZOID: {fu1}, liší se: {a1 - fu1}")
print(f"ROMBERG: {fu2}, liší se: {a1 - fu2}")
print(f"SIMPSON: {fu3}, liší se: {a1 - fu3}")
print(f"GAUSS: {fu4}, liší se: {a1 - fu4}")

#Funkce 2
print("Funkce: 3*x -e^(4*x)")
a1 = analytic(f2, a, b)
fu1 = trapeziod(f2, a, b, dx)
fu2 = romberg(f2, a, b)
fu3 = simpson(f2, a, b, dx)
fu4 = rieman(f2, a, b)
print(f"TRAPEZOID: {fu1}, liší se: {a1 - fu1}")
print(f"ROMBERG: {fu2}, liší se: {a1 - fu2}")
print(f"SIMPSON: {fu3}, liší se: {a1 - fu3}")
print(f"GAUSS: {fu4}, liší se: {a1 - fu4}")

#Funkce 3
print("Funkce: 2*sin(-2*x+2)")
a1 = analytic(f3, a, b)
fu1 = trapeziod(f3, a, b, dx)
fu2 = romberg(f3, a, b)
fu3 = simpson(f3, a, b, dx)
fu4 = rieman(f3, a, b)
print(f"TRAPEZOID: {fu1}, liší se: {a1 - fu1}")
print(f"ROMBERG: {fu2}, liší se: {a1 - fu2}")
print(f"SIMPSON: {fu3}, liší se: {a1 - fu3}")
print(f"GAUSS: {fu4}, liší se: {a1 - fu4}")

