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

if fh > 40 :
# Overtime Pay
    fp = (fh-40.0)*fr*1.5+40.0*fr
    print("Pay:",fp)
else : 
# Regular Pay
    fp = fh*fr
    print("Pay:",fp)