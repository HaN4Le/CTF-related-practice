# -*-  coding: utf-8  -*-

Plaintext_list = {".-": 'A', "-...":'B', "-.-.":'C', "-..":'D', ".":'E', "..-.":'F', "--.":'G',
    "....":'H', "..":'I', ".---":'J', "-.-":'K', ".-..":'L', "--":'M', "-.":'N', "---":'O', ".--.":'P',
    "--.-":'Q', ".-.":'R', "...":'S', "-":'T', "..-":'U', "...-":'V', ".--":'W', "-..-":'X', "-.--":'Y',
    "--..":'Z', ".----":"1", "-----":'0', "..---":"2", "...--":'3', "....-":"4", ".....":"5", "-....":"6", 
    "--...":"7", "---..":"8", "----.":"9", "--..--":',', ".-.-.-":'.', "---...":":", "-.-.-.":";","..--..":"?",
    "-...-":"=", ".----.":"'", "-..-.":"/", "-.-.--":"!", "-....-":"-","..--.-":"_",".-..-.":"\"","-.--.":"(",
    "-.--.-":")", "...-..-":"$",".-...":"&",".--.-.":"@",".-.-.":"+"
}

Ciphertext_list = {v : k for k, v in Plaintext_list.items()}                        # 使得 Plaintext_list 字典的 key 值和 value 的反过来


def decrypt(Ciphertext):
    newCiphertext = ""
    if Ciphertext[0] == "1":
        for i in Ciphertext:
            if i == "1":
                i = "-"
                newCiphertext += ("").join(i)
            elif i == "0":
                i = "."
                newCiphertext += ("").join(i)
            else:
                i = " ..--.- "
                newCiphertext += ("").join(i)
        print("[+] newCiphertext is: ",newCiphertext)
            
    try:
        split_Ciphertext = Ciphertext.split(" ")
        #split_Ciphertext = newCiphertext.split(" ")                                    # 将得到的摩斯密文字符串按照空格进行划分
        print("[+] Ciphertext is: ",split_Ciphertext)
        Plaintext = ""
        for j in split_Ciphertext:
            Plaintext += ("").join(Plaintext_list[j].lower())                       # 遍历划分后的密文数组，使得按照字典“decryption_list”中的对应关系进行映射
        print("[+] Plaintext is: ", Plaintext.replace("_"," "))
    except:
        print("[-] Please input legal Ciphertext.")

def encrypt(Plaintext):
    try:
        Ciphertext = ""
        for j in Plaintext.upper():
            Ciphertext += ("").join(Ciphertext_list[j] + " ")
        print("Ciphertext is: ", Ciphertext)
    except:
        print("Please input legal Plaintext.")


if __name__ == "__main__":
    print("******************** Description：Enter Morse cipher text with space ********************")
    print("Please choose the function 1 or 2:")
    print("1.Decrypt Morse Code.")
    print("2.Encrypt Morse Code.")
    function_choose = input("Choose the function: ")
    string_input = input("Input: ")
    string_input = string_input.replace("/", " ")
    try:
        if function_choose == "1":
            decrypt(string_input)
        elif function_choose == "2":
            encrypt(string_input)
    except:
        print("Please choose correctly the function that you want to do.")