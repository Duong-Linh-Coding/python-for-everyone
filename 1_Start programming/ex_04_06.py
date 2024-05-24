def computepay(fh, fr) :
    if fh > 40 :
    # Overtime Pay
        fp = (fh-40.0)*fr*1.5+40.0*fr
    else :
    #regular pay
        fp=fh*fr
    #print("Returning",fp)
    return fp

sh = input("Enter Hours: ")
# Try & Except
try:
    fh = float(sh)
except:
    print("Error, please enter numeric input")
    quit()
sr = input("Enter Rate: ")
# Try & Except
try:
    fr = float(sr)
except:
    print("Error, please enter numeric input")
    quit()
    
fp = computepay(fh,fr)
print ("Pay:", fp)