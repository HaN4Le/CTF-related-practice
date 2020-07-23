# -*- coding: utf-8 -*-


base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64encode(Plaintext):
    bin_Plaintext = ""                                                              # 存储明文的二进制字符串
    bin_Ciphertext = ""                                                             # 存储编码后二进制字符串（为了方面下文统称为密文，答案这种叫法有些不妥）
    Ciphertext = ""                                                                 # 存储密文

    # for 循环，遍历明文中的字符，将每个字符转换为二进制的形式，并赋值给 bin_Plaintext
    for i in Plaintext:
        bin_Plaintext += ("").join(bin(ord(i)).replace("0b", "").zfill(8))
    len_bin = len(bin_Plaintext) / 6                                                # 将明文二进制字符串的长度除以 6 
    # print(len_bin)
    # print("bin_Plaintext is :",bin_Plaintext)
    anly_condition = len(bin_Plaintext) % 6                                         # 计算明文二进制字符串的长度是否为 6 的倍数

    # 条件判断语句：如果明文二进制的长度是 6 的倍数，说明末尾无需增加“=”，直接按照每 6 个为一单位，寻找对应的“密文“
    if not anly_condition:
        for i in range(0, len(bin_Plaintext), 6):                                   # 从 0 开始，到二进制字符串的长度为结尾，step 为 6
            # bin_Ciphertext += ("").join(bin_Plaintext[i:i+6])                     # 将 bin_Plaintext 索引为 i 到 i + 6 的字符全部添加到 bin_Ciphertext 中
            # Ciphertext += ("").join(base64chars[int(bin_Ciphertext,2)])
            # bin_Ciphertext = ""
            Ciphertext += ("").join(base64chars[int(bin_Plaintext[i:i+6], 2)])      # 是上面三行的综合
    else:
        # 思路：
        Reg = 0
        len_Ciphertext = (int(len_bin) + 1) * 6
        new_bin_Plaintext = bin_Plaintext.ljust(len_Ciphertext, "0")
        anly_condition_nums = len(new_bin_Plaintext) % 8
        while anly_condition_nums:
            new_bin_Plaintext = bin_Plaintext.ljust(6 + len(new_bin_Plaintext), "0")
            anly_condition_nums = len(new_bin_Plaintext) % 8
            Reg += 1
        # print(new_bin_Plaintext)
        new_bin_Plaintext = bin_Plaintext.ljust(len_Ciphertext, "0")
        # print("new_bin_Plaintext :",new_bin_Plaintext)
        for i in range(0, len(new_bin_Plaintext), 6):
            bin_Ciphertext += ("").join(new_bin_Plaintext[i:i+6])
            # print("bin_Ciphertext is:", "0b" + bin_Ciphertext)
            Ciphertext += ("").join(base64chars[int(bin_Ciphertext, 2)])
            bin_Ciphertext = ""
        # print("Reg is:",Reg)
        if Reg == 1:
            Ciphertext += ("").join("=")
        elif Reg == 2:
            Ciphertext += ("").join("==")
    print("base64encode'result is: ",Ciphertext)
        
def base64decode(Ciphertext):
    bin_Ciphertext = "" 
    Plaintext = ""
    end_delete_num = Ciphertext.count("=")
    Ciphertext = Ciphertext.replace("=", "")
    for i in Ciphertext:
        bin_Ciphertext += ("").join(bin(base64chars.find(i)).replace("0b", "").zfill(6))
    # print(bin_Ciphertext)
    if end_delete_num:
        bin_Ciphertext = bin_Ciphertext[:-2*end_delete_num]
    for i in range(0, len(bin_Ciphertext), 8):
        Plaintext += ("").join(chr(int(bin_Ciphertext[i:i+8], 2)))

    print("base64decode's result is:",Plaintext)


if __name__ == "__main__":
    print("Please input the function:")
    print("1：base64encode.")
    print("2：base64decode.")
    function_choose = input("Please choose the function：")
    str_input = input("Input：")

    # 选择编码和解码的功能
    if function_choose == "1":
        base64encode(str_input)
    else:
        base64decode(str_input)