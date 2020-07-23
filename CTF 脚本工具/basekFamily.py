# -*- coding: utf8 -*-
import base64

def baseFamily(encodetext):
    i = 0
    while True:
        i += 1
        try:
            encodetextCopy = base64.b64decode(encodetext)
        except:
            pass
        else:
            print("[*] base64decode:",str(encodetextCopy,encoding="utf8"))
            encodetext = encodetextCopy
            continue
        try:
            encodetextCopy = base64.b32decode(encodetext)
        except:
            pass
        else:
            print("[*] base64decode:",str(encodetextCopy,encoding="utf8"))
            encodetext = encodetextCopy
            continue
        try:
            encodetextCopy = base64.b16decode(encodetext)
        except:
            pass
        else:
            print("[*] base64decode:",str(encodetextCopy,encoding="utf8"))
            encodetext = encodetextCopy
            continue
        break

if __name__ == "__main__":
    encodetext = input("[?] Please input encode text：")
    baseFamily(encodetext)