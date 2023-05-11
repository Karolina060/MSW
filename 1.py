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
print(f"{vysledek_m}")
print(f"a výpočet trvá {(konec_m - start_m)} sekund.")
print("\n")

#násobení matic pomocí cyklu for
start_m2 = process_time()
matice_m2 = [[1, 2, 3], [2, 6, 4], [9, 4, 8]]
for i in range(len(matice_m2)):
    for j in range(len(matice_m2[0])):
        matice_m2[i][j] = matice_m2[i][j]*12
konec_m2 = process_time()

print(f"Násobení matice pomocí cyklu for. Matice je")
print(f"{matice_m2}")
print(f"Výpočet trvá {(konec_m2 - start_m2)} sekund.")
print("\n")

rozdil_m = (konec_m - start_m)-(konec_m2 - start_m2)

print(f"Rozdíl v časech je {rozdil_m} sekund.")

if rozdil_m > 0:
    print(f"Násobení pomocí cyklu for je rychlejší.")
elif rozdil_m < 0:
    print(f"Násobení pomocí knihovny numpy je rychlejší.")
else:
    print(f"Čas výpočtu je stejný.")
print("\n")


#faktorial
start_f = process_time()
x = 218
vysledek_f = factorial(x)
konec_f = process_time()
vysledek_f= str(vysledek_f)

print(f"Faktorial z čísla {x} je {vysledek_f[:10]}.")
print(f"Výpočet trvá {(konec_f - start_f)} sekund.")
print("\n")

#výpočet faktoriálu pomocí cyklu for
start_f2 = process_time()
x2 = 218
vysledek_f2 = 1
for i in range(1, x2+1):
    vysledek_f2 = vysledek_f2 * i
konec_f2 = process_time()
vysledek_f2 = str(vysledek_f2)

print(f"Faktoriál čísla {x2} je {vysledek_f2[:10]}.")
print(f"Výpočet trvá {(konec_f2 - start_f2)} sekund.")
print("\n")

rozdil_f = (konec_f - start_f)-(konec_f2 - start_f2)

print(f"Rozdíl v časech je {rozdil_f} sekund.")

if rozdil_f > 0:
    print(f"Výpočet faktoriálu pomocí cyklu for je rychlejší.")
elif rozdil_f < 0:
    print(f"Výpočet faktoriálu pomocí knihovny numpy je rychlejší.")
else:
    print(f"Čas výpočtu je stejný.")
print("\n")


#skalarní součin
start_s = process_time()
vekt_1 = np.array([25, 35, 45])
vekt_2 = np.array([3, 6, 9])
vysledek_s = sum(vekt_1*vekt_2)
konec_s = process_time()

print(f"Skalární součin je roven {vysledek_s}.")
print(f"Výpočet trvá {(konec_s - start_s)} sekund.")
print("\n")

#skalární součin pomocí cyklu for
start_s2 = process_time()
vysledek_s2 = 0
a2 = (25, 35, 45)
b2 = (3, 6, 9)
for i in range(len(a2)):
    vysledek_s2 += a2[i]*b2[i]
konec_s2 = process_time()

print(f"Skalární součin je {vysledek_s2}.")
print(f"Výpočet trvá {(konec_s2 - start_s2)} sekund.")
print("\n")

rozdil_s = (konec_s - start_s)-(konec_s2 - start_s2)

print(f"Rozdíl v časech je {rozdil_s} sekund.")

if rozdil_s > 0:
    print(f"Skalární součin pomocí cyklu for je rychlejší.")
elif rozdil_s < 0:
    print(f"Skalární součin pomocí knihovny numpy je rychlejší.")
else:
    print(f"Čas výpočtu je stejný.")
print("\n")

#derivace sympy
def derivace_sym(funkce, promenna, hodnota):
    prom = symbols("x")
    deri = diff(funkce, promenna)
    return (deri.subs(x, hodnota)).doit()
    
start_d = process_time()
x = symbols('x')
funkce_d = -3*x**5+2*x**4+8*x-3+18*x**2-10*x-23
vysledek_d = derivace_sym(funkce_d, x, 7)

konec_d = process_time()

print(f"Derivace je {vysledek_d}.")
print(f"Výpočet trvá {(konec_d - start_d)} sekund.")
print("\n")

#derivace pomocí funkce
funkce_d2 = -3*x**5+2*x**4+8*x-3+18*x**2-10*x-23
def f(x2):
    return -3*x**5+2*x**4+8*x-3+18*x**2-10*x-23
def derivace(funkce_d2, hodnota, h=0.01):
    return (funkce_d2(hodnota+h) - funkce_d2(hodnota))/h
start_d2 = process_time()
vysledek_d2 = derivace(f, 10)
konec_d2 = process_time()

print(f"Derivace je {vysledek_d2}.")
print(f"Výpočet trvá {(konec_d2 - start_d2)} sekund.")
print("\n")

rozdil_d = (konec_d - start_d)-(konec_d2 - start_d2)

print(f"Rozdíl v časech je {rozdil_d} sekund.")

if rozdil_d > 0:
    print(f"Derivace pomocí funkce je rychlejší.")
elif rozdil_d < 0:
    print(f"Derivace pomocí knihovny sympy je rychlejší.")
else:
    print(f"Čas výpočtu je stejný.")
print("\n")


#integrál scipy
start_i = process_time()
vysledek_i = integrate.quad(lambda x: (5*x**4-10*x**3+3*x**2-8*x-20), 3, 6)
konec_i = process_time()

print(f"Výpočet integrálu je {vysledek_i[0]}.")
print(f"Výpočet trvá {(konec_i - start_i)} sekund.")
print("\n")

#integrál pomocí funkce
def g(x2):
    return 5*x**4-10*x**3+3*x**2-8*x-20
start_i2 = process_time()
vysledek_i2 = 0
ai2 = 3
bi2 = 6
dx = 0.0001
while ai2 < bi2:
    vysledek_i2 += dx * (g(x2) + f((ai2+dx)))/2
    ai2 += dx
konec_i2 = process_time()

print(f"Integrace je {vysledek_i2}.")
print(f"Výpočet trvá {(konec_i2 - start_i2)} sekund.")
print("\n")

rozdil_i = (konec_i - start_i)-(konec_i2 - start_i2)

print(f"Rozdíl v časech je {rozdil_i} sekund.")

if rozdil_i > 0:
    print(f"Integrace pomocí funkce je rychlejší.")
elif rozdil_i < 0:
    print(f"Integrace pomocí knihovny scipy je rychlejší.")
else:
    print(f"Čas výpočtu je stejný.")
print("\n")



