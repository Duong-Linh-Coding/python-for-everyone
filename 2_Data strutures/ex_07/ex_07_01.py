fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("Invalid filename")
    quit()
    
for linex in fhand:
    liney = linex.rstrip()
    print(liney.upper())