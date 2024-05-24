fhand = open("mbox-short.txt")
count = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if not line.startswith("From ") : continue
#    print(line)
    word = words[1]
#    print(word)
    count[word] = count.get(word,0) + 1
#print("Mail",count)
#print(count)

biggest_mailmess = None
biggest_count = None
for mail,mailcount in count.items():
    if biggest_count is None or mailcount > biggest_count :
        biggest_mailmess = mail
        biggest_count = mailcount
        
print(biggest_mailmess,biggest_count)