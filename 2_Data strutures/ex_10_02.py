name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = {}
lst = []

for line in handle:
    line = line.rstrip()
#    print(line)
    words = line.split()
    if not line.startswith("From ") : continue
    word = words[5]
    hours = word.split(":")[0]
    print(hours)
    counts[hours] = counts.get(hours, 0 ) + 1
print(counts)
  
for hour, time in sorted(counts.items()):
    print(hour,time)