# -*- coding: utf-8 -*-
# This is the program that aimed at decrypt and encrypt of rot-13

def Encryption(Plaintext):
    Cipher_text = ''
    for i in Plaintext:
        if ord(i) <= 90 and ord(i) >= 65:
            i = ord(i) + 13
            if i > 90:
                i = 64 + i % 90
                Cipher_text += ("").join(chr(i))
            else:
                Cipher_text += ("").join(chr(i))
        elif ord(i) <= 122 and ord(i) >= 97:
            i = ord(i) + 13
            if i > 122:
                i = 96 + i % 122
                Cipher_text += ("").join(chr(i))
            else:
                Cipher_text += ("").join(chr(i))
        else:
            Cipher_text += ("").join(i)
    
    print("The Ciphertext is:", Cipher_text)

def Decryption(Ciphertext):
    Plain_text = ""
    for i in Ciphertext:
        if ord(i) <= 90 and ord(i) >= 65:
            i = ord(i) - 13
            if i < 65:
                i = 91 - 65 % i
                Plain_text += ("").join(chr(i))
            else:
                Plain_text += ("").join(chr(i))
        elif ord(i) <= 122 and ord(i) >= 97:
            i = ord(i) - 13
            if i < 97:
                i = 123 - 97 % i
                Plain_text += ("").join(chr(i))
            else:
                Plain_text += ("").join(chr(i))
        else:
            Plain_text += ("").join(i)
    print("The Plaintext is:", Plain_text)


if __name__ == "__main__":
    print("Please choose the function:")
    print("1:Encryption")
    print("2:Decryption")
    fct = int(input())
    if fct == 1:
        Plaintext = input("Please input Plaintext:")
        Encryption(Plaintext)
    elif fct == 2:
        Ciphertext = input("Please input Ciphertext:")
        Decryption(Ciphertext)
    else:
        print("Please input correct number :)")