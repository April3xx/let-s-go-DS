import os,sys
filename = input('filenamebro : ')
bruda = 0
with open('C:\\Users\\priva\\Downloads\\errorslogdecrypt.txt','r') as f:
    mamamea = f.readlines()
    for lines in mamamea:
        if lines[0] == '[' : bruda+=1
        print (lines[0])
print(bruda)