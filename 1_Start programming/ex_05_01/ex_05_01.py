count = 0
summ = 0
while True:
    sline = input("Enter a number: ")
#End loop
    if sline == "done" :
        break
#Error check
    try:
        fline = float(sline)
    except:
        print("Invalid input")
        continue
    count = count + 1
    summ = summ + fline
            
print (summ,count,summ/count)