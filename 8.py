#derivace
def forward_derivate(f, x0, k):
    return (f(x0+k) - f(x0))/k

def backward_derivate(f, x0, k):
    return (f(x0) - f(x0-k))/k

def central_derivate(f, x0, k):
    return (f(x0+k) - f(x0-k))/(2*k)

def forward_derivate_adaptive(f, x0, adaptive_k):
    return (f(x0+adaptive_k) - f(x0))/adaptive_k

def backward_derivate_adaptive(f, x0, adaptive_k):
    return (f(x0) - f(x0-adaptive_k))/adaptive_k

def central_derivate_adaptive(f, x0, adaptive_k):
    return (f(x0+adaptive_k) - f(x0-adaptive_k))/(2*adaptive_k)

#funkce
f = lambda x: x**4 + 2*x**3 - 6
x0 = 3
k = 0.1
adaptive_k = float(input("Zadej adaptivní krok (nejlépe od 0 do 1): "))
print("\n")

forw_de = forward_derivate(f, x0, k)
back_de = backward_derivate(f, x0, k)
cent_de = central_derivate(f, x0, k)
forw= forward_derivate_adaptive(f, x0, adaptive_k)
back = backward_derivate_adaptive(f, x0, adaptive_k)
cent = central_derivate_adaptive(f, x0, adaptive_k)

#výsledek
print(f"Dopředná bez kroků: {forw_de}, dopředná s krokem: {forw}, rozdíl = {abs(forw_de- forw)}")
print("\n")
print(f"Zpětná bez kroků: {back_de}, zpětná s krokem: {back}, rozdíl = {abs(back_de - back)}")
print("\n")
print(f"Centrální bez kroků: {cent_de}, centrální s krokem: {cent}, rozdíl = {abs(cent_de - cent)}")
print("\n")