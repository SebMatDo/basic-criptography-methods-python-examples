#!/usr/bin/env python3

import math

def powmod(base, exp, mod):
    """
    Calculates (base^exp) % mod efficiently using modular exponentiation.
    """
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

# Source - https://stackoverflow.com/a
# Posted by John Coleman, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-19, License - CC BY-SA 3.0

def baby_steps_giant_steps(a,b,p,N = None):
    if not N: N = 1 + int(math.sqrt(p))

    #initialize baby_steps table
    baby_steps = {}
    baby_step = 1
    for r in range(N+1):
        baby_steps[baby_step] = r
        baby_step = baby_step * a % p

    #now take the giant steps
    giant_stride = pow(a,(p-2)*N,p)
    giant_step = b
    for q in range(N+1):
        if giant_step in baby_steps:
            return q*N + baby_steps[giant_step]
        else:
            giant_step = giant_step * giant_stride % p
    return "No Match"

def bruteLog(b, c, m):
    s = 1
    for i in range(m):
        s = (s * b) % m
        if s == c:
            return i + 1
    return -1

# Example Usage:
if __name__ == "__main__":
    # Find k such that 2^k = 3 (mod 5)
    print("Devuelve el logaritmo discreto o nada")
    base = int(input("escriba la base como un entero: "))
    resultado = int(input("Escriba el resultado como un entero: "))
    modulo = int(input("escriba el modulo como un entero: "))
    #N = None
    #N = int(input("Escriba el tope maximo como un entero, puede dejarse nulo: "))
    res = baby_steps_giant_steps(base,resultado,modulo)
    print("Resultado: ", res)
    resBrute= bruteLog(base,resultado,modulo)
    print("Resultado por brute force: ",resBrute)