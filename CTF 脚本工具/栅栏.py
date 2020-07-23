# -*- coding: utf8 -*-

def RailfenceEnc(Plaintext):
    length = len(Plaintext)
    index = 1
    ciphertext = ""
    ciphertext_list = []
    ciphertext_str = ""
    for row in range(2, length):
        if not(length%row):
            print("[?] 第%d情况：" % index) 
            row_size = length // row
            for i in range(0, row):
                print("[*] Row %d :" % (i+1), end="")
                for j in range(0, row_size):
                    ciphertext_str += ("").join(Plaintext[i+j+(row_size-1)*i])
                    print(Plaintext[i+j+(row_size-1)*i]," ",end="")
                    # print("i+j+row_size*i:",i+j+(row_size-1)*i," ",end="")
                print(end="\n")
                ciphertext_list.append(ciphertext_str)
                ciphertext_str = ""
            index += 1
            for i in range(0, row_size):
                for j in range(0, row):
                    ciphertext += ("").join(ciphertext_list[j][i])
            print("[+] The ciphertext is: ",ciphertext)
            ciphertext_list = []
            ciphertext = ""
            print(end="\n")

def RailfenceDec(ciphertext):
    index = 1
    length = len(ciphertext)
    Plaintext = ""
    Plaintext_list = []
    Plaintext_str = ""
    for row in range(2, length):
        if not(length%row):
            print("[?] 第%d情况：" % index)
            row_size = length // row
            for i in range(0,row):
                print("[*] Row %d :" % (i+1), end="")
                for j in range(0,row_size):
                    Plaintext_str += ("").join(ciphertext[i+j+(row_size-1)*i])
                    print(ciphertext[i+row*j],end="")
                    
                print(end="\n")
                Plaintext_list.append(Plaintext_str)
                Plaintext_str = ""
            index += 1
            for i in range(0, row_size):
                for j in range(0, row):
                    Plaintext += ("").join(Plaintext_list[j][i])
            print("[+] The Plaintext is: ", Plaintext)
            Plaintext_list = []
            Plaintext = ""
            print(end="\n")

if __name__ == "__main__":
    
    print("[+] Welcome to Railfence world!")
    print("[?] Please input the number of function:")
    print("[+] 1:encryption")
    print("[+] 2:decryption")
    while True:
        try:
            function = input("[?] ")
            function = int(function)
            if (function != 1 and function != 2):
                print("[+] Please choose correct function.")
                continue
        except ValueError:
            print("[+] Please input legitimate function.")
            continue
        else:
            
         
            string = input("[?] Please input your string:")
        
        if function == 1:
            RailfenceEnc(string)
        else:
            RailfenceDec(string)
        
        break
     