sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
if fh > 40 :
# Overtime Pay
    fp = (fh-40.0)*fr*1.5+40.0*fr
    print("Pay:",fp)
else : 
# Regular Pay
    fp = fh*fr
print("Pay:",fp)