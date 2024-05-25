fname = input("Enter a file name: ")
count = 0
summ = 0
try:
    fhand = open(fname)
except:
#    print("Invalid filename")
    quit()
    
for linex in fhand :
    liney = linex.rstrip()
    pieceline = liney[(liney.find(":"))+1:]
    if not "X-DSPAM-Confidence:" in linex :
        continue
#    print(liney)
    fpieceline = float(pieceline)
    print(fpieceline)
    count = count + 1
    summ = summ + fpieceline
    
print(summ/count)