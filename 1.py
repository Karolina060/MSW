import numpy as np
import timeit
from sympy import *
import scipy.integrate as integrate
from math import factorial
from time import process_time

#nasobeni matic 
start_m = process_time()
matice = [[1, 2, 3], [2, 6, 4], [9, 4, 8]]
vysledek_m = np.array(matice)*12
konec_m = process_time()

print(f"Matice je") 
print(f"{vysledek_m} ")
print(f"a výpočet trvá {(konec_m - start_m)} sekund.")

#faktorial
start_f = process_time()
x = 218
vysledek_f = factorial(x)
konec_f = process_time()
vysledek_f= str(vysledek_f)

print(f"Faktorial z čísla {x} je {vysledek_f[:10]}.")
print(f"Výpočet trvá {(konec_f - start_f)} sekund.")


#skalarní součin
start_s = process_time()
vekt_1 = np.array([25, 35, 45])
vekt_2 = np.array([3, 6, 9])
vysledek_s = sum(vekt_1*vekt_2)
konec_s = process_time()

print(f"Skalární součin je roven {vysledek_s}.")
print(f"Výpočet trvá {(konec_s - start_s)} sekund.")

#derivace
def derivace_sym(funkce, promenna, hodnota):
    prom = symbols("x")
    deri = diff(funkce, promenna)
    return (deri.subs(x, hodnota)).doit()
    
start_d = process_time()
x = symbols('x')
funkce_d = -3*x**5+2*x**4+8*x-3+18*x**2-10*x-23
vysledek_d = derivace_sym(funkce, x, 7)

konec_d = process_time()

print(f"Derivace je {vysledek_d}.")
print(f"Výpočet trvá {(konec_d - start_d)} sekund.")


#integrál
start_i = process_time()
vysledek_i = integrate.quad(lambda x: (3*x**2-6*x+3), 1, 5)
konec_i = process_time()

print(f"Výpočet integrálu je {vysledek_i[0]}.")
print(f"Výpočet trvá {(konec_i - start_i)} sekund.")
