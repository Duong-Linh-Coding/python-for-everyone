import re
hand = open("regex_sum_42.txt.crdownload")
summ = []
for line in hand:
    #print(line)
    line = line.rstrip()
    num = re.findall("[0-9]+", line)
    fnum = list(map(int,num))
    if len(fnum)<0 : continue
    #print(fnum)
    summ.extend(fnum)
print(summ)
print(sum(summ))