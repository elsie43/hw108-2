f = open('0504hw.txt', 'r+')

#count line
lnum = 0
wnum = 0
wwnum = 0
for line in f:
    #print(line, end = '\n')
    lnum = lnum + 1
    for i in line:
        if i not in ['\n']:
            wwnum += 1
        if i not in ['，','；','。','\n',' ']:
            wnum += 1

print('\n此檔案共',lnum,'行\n')
print('不含標點符號共',wnum,'字\n')
print('含標點符號共',wwnum,'字\n')
f.close()
