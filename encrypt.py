


import random

def encryptFile():
    file = input("Enter file name: ")
    with open(file,"r+") as fileRead:
        content = fileRead.readlines()


    key = []
    encrypted = []
    for lines in content:
        num = random.randrange(1,100)
        letter = random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        keyline =f'{num},{letter}'
        key.append(keyline)
        word = ""
        for line in lines:
            #print(line)
            word += str(ord(line)/(num+ord(letter[0]))) + "-"
        
            
        data = f'{word}{letter[0]}'
        #print(data)
        encrypted.append(data)


    with open("keys.keys","w+") as keys,open("content.keys","w+") as file:
        for kes,encrypts in zip(key, encrypted):
            keys.write(kes+'\n')
            file.write(encrypts+'\n')
        
        


encryptFile()
        
    
    
    

