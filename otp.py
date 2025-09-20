#!/usr/bin/env python3

def otp_encrypt(message, key):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    cifrado = ""
    for i in range(len(message)):
        m = message[i].upper()
        k = key[i].upper()
        if m not in alfabeto or k not in alfabeto:
            raise ValueError("El mensaje y la clave deben contener solo letras del alfabeto español (A-Z, Ñ).")
        m_idx = alfabeto.index(m)
        k_idx = alfabeto.index(k)
        e_idx = (m_idx + k_idx) % len(alfabeto)
        cifrado += alfabeto[e_idx]
    return cifrado


def otp_decrypt(ciphertext, key):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    descifrado = ""
    for i in range(len(ciphertext)):
        c = ciphertext[i].upper()
        k = key[i].upper()
        if c not in alfabeto or k not in alfabeto:
            raise ValueError("El texto cifrado y la clave deben contener solo letras del alfabeto español (A-Z, Ñ).")
        c_idx = alfabeto.index(c)
        k_idx = alfabeto.index(k)
        m_idx = (c_idx - k_idx) % len(alfabeto)
        descifrado += alfabeto[m_idx]
    return descifrado


def main():
    opcion = input("Seleccione una opción: cifrar (E) o descifrar (D): ").strip().upper()
    mensaje = input("Ingrese el mensaje (solo letras A-Z y Ñ, sin espacios): ").replace(" ", "").upper()
    clave = input("Ingrese la clave (solo letras A-Z y Ñ, al menos tan larga como el mensaje): ").replace(" ", "").upper()
    if len(clave) < len(mensaje):
        print("Error: La clave debe ser al menos tan larga como el mensaje.")
        return
    if opcion == 'E':
        cifrado = otp_encrypt(mensaje, clave)
        print("Cifrado:", cifrado)
    elif opcion == 'D':
        descifrado = otp_decrypt(mensaje, clave)
        print("Descifrado:", descifrado)
    else:
        print("Opción inválida. Seleccione 'E' para cifrar o 'D' para descifrar.")

if __name__ == "__main__":
    main()