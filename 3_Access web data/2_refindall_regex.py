import re
hand = open("regex_sum_2022522.txt.crdownload")
summ = []
for line in hand:
    #print(line)
    line = line.rstrip()
    num = re.findall("[0-9]+", line)
# num return strings => convert to int
    fnum = list(map(int,num))
    if len(fnum)<0 : continue
    #print(fnum)
    summ.extend(fnum)
print(summ)
print(sum(summ))