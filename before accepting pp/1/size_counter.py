import os,sys
filename = input('filenamebro : ')
bruda = 0
with open('D:\\Users\\phoom\\Documents\\GitHub\\let-s-go-DS\\1\\size_decrypt 1GB.txt','r') as f:
    mamamea = f.readlines()
    for lines in mamamea:
        bruda += int(lines)/1073741824
print(bruda)
#decrypt 71.90111409127712
#encrypt 56.95995719823986
#max int can count file upto 8388608 TB
# print(sys.maxsize/1099511627776)
#28.3(otherdrives) + 117(all in c) - 24.3(windows) = 56(all encrypted)
