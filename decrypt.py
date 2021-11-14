


def Decrypt():
    file = input("Enter file name: ")
    with open(file,"r+") as fileRead, open("keys.keys","r+") as keys:
        content = fileRead.readlines()
        key = keys.readlines()

    
    #print(content)
    #print(key)
    words = ""
    for keyd, line in zip(key,content):
        keycont = keyd.split(",")
        keyss = keycont[1][2]
        #print(keyss)
        keyss = keyss.replace("\n","")
        if line.find(keyss) > -1:
            newline = line[:line.find(keyss)]
            datum = newline.split("-")
            for word in datum:
                if word == '':
                    pass
                else:
                    data = float(word) * (int(keycont[0]) + ord(keyss))
                    #print(" ==== ",data, "-----",int(data),"<<<<<",chr(int(data)))
                    if data == int(data):
                        words += chr(int(data))
                    else:
                        data = round(data,1)
                        words += chr(int(data))
                        
            print(words)
            
        else:
            print('Key is not valid')
        
    




Decrypt()
