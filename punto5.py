n : int = int(input("Introduce un número natural: "))
factorial = 1
f = 1
while f <= n:
    factorial *= f
    f += 1
print(n,"! es =", factorial)