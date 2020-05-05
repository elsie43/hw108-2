f = open('0504hw.txt', 'r+') #pwd 0504file 

lnum = 0 #count line
wnum = 0 #count character except[...]
wwnum = 0 #count all character
for line in f: #line
    lnum = lnum + 1
    for i in line:
        if i not in ['，','；','。','\n',' ','！','？']:
            wnum += 1
        if i not in ['\n',' ']:
            wwnum += 1

print('\n此檔案共',lnum,'行\n')
print('不含標點符號共',wnum,'字\n')
print('含標點符號共',wwnum,'字\n')
f.close()
