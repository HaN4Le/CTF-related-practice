# -*- coding: utf8 -*-

def caesar(ciphertext):
    newString = ""
    for j in range(1,26):
        for i in ciphertext:
            if ord(i) > 96 and ord(i) < 123:
                if ord(i)+j > 122:
                    newString += ("").join(chr((ord(i)+j)%123+97))
                else:
                    newString += ("").join(chr((ord(i)+j)))
            elif ord(i) > 65 and ord(i) < 91:
                if ord(i)+j > 90:
                    newString += ("").join(chr((ord(i)+j)%91+65))
                else:
                    newString += ("").join(chr((ord(i)+j)))
            else:
                newString += ("").join(i)
            
        print("[+] Offset is ",j)
        print("[+] Plaintext is",newString)
        newString = ""






if __name__ ==  "__main__":
    ciphertext = input("Please input the ciphertext of caesar:")
    plaintext = caesar(ciphertext)