xh=input("Enter Hour: ")
try: 
    ival = int(xh)
except: 
    ival = -1
if ival > 0 :
    print ("")   
else:
    print ("Not a Number") 
xr=input("Enter rate: ")
try: 
    iral = int(xr)
except: 
    iral = -1
if iral > 0 :
    print ("")   
else:
    print ("Not a Number") 
if int(xh) > 40 :
    xp = 40 * int(xr) + (int(xh) - 40)*1.5*int(xr)
print("Pay",xp) 