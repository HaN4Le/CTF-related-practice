import os

def judgmentfileFormat(fileFormat):
    formatDictionary = ["html","txt","text","php","js","py","c","htm"]
    if fileFormat in formatDictionary:
        return 1
    else:
        return 0

def fileList(dir,fileFormat):
    a = 0
    b = 0
    oldText = input("[*] Enter the old content you want to replace:")
    newText = input("[*] Enter the new content you want to replace:")
    for dirpath, dirs, files in os.walk(dir):
        #print("#######dir list#######")
        for fileName in files:
            #print("1")
            if fileName[len(fileName)-len(fileFormat):len(fileName)] == fileFormat:
                a += 1                
                filePath = dirpath + "\\" + fileName
                print(filePath)
                file_data = ""
                with open(filePath,"r",encoding="utf-8") as f1:
                    for line in f1:
                        if oldText in line:
                            line = line.replace(oldText,newText)
                            b += 1
                        file_data += line
                with open(filePath,"w",encoding="utf-8") as f2:
                    f2.write(file_data)
    print("[+] A total of", a, fileFormat, "format files were searched.")
    if b:
        print("[+] A total of", b, "files have been modified.")
        print("[+] Have done! :)\n")
    else:
        print("[+] Sorry :( the files don't include the context you want to change.\n")
    
                    
        #print("#######dir list#######")
'''
        print("#######file list#######")
        for filename in files:
            print(filename)
            fullname = os.path.join(home, filename)
            print(fullname)
        print("#######file list#######")
'''
if __name__ == "__main__":
    print("\n******************************************************************\n")
    print("  Modify the the context of the file format you want to change.")
    print("  We can process the file formats are: ")
    print("  [1] html\n  [2] txt\n  [3] text\n  [4] php\n  [5] js\n  [6] py\n  [7] c\n  [8] htm")
    print("\n******************************************************************\n")
    path = input("[*] Please enter the file path:")
    fileFormat = input("[*] Please enter the file type of the file you want to change:")
    resultFile = judgmentfileFormat(fileFormat)
    if not resultFile:
        print("[+] Sorry we can't process the file. GoodBye!\n")
        exit()
    fileList(path,fileFormat)