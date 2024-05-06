import numpy as np

def metodo(e):
    return e

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])

d = np.array([a,b,c])

x = metodo(d)
"""
for e in d:
    print("",end="-")
    print(e,end="-")
print("")
"""
print(np.ndenumerate(x))
x,y,z = a
print(x,y,z)

for i,v in np.ndenumerate(x):
    print(i)
    print(v)

"""for e in x:
    print("",end="-")
    for a in e:
        print(a,end="-")
    print("")
"""
for i,v in np.ndenumerate(x):
    print(i)
    print(v)

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

for indice in np.ndenumerate(matriz):
    print(f"Índice: {indice}")

for indice, valor in np.ndenumerate(matriz):
    print(f"Índice: {indice}, Valor: {valor}")