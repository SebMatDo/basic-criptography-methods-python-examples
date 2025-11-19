#!/usr/bin/env python3

# Modular exponentiation
def power_mod(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c

def main():
    print("Este programa devuelve el power mod")
    base = int(input("Escriba la base como un entero: "))
    exponente = int(input("Escriba el exponente como un entero: "))
    modulo = int(input("Escriba el modulo como un entero: "))
    res = power_mod(base,exponente,modulo)
    print("resultado: ",res)


if __name__ == "__main__":
    main()