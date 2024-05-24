strex = 'X-DSPAM-Confidence: 0.8475 '
ex = strex.find(":")
#print(ex)
piece = strex[ex+1:]
#print(piece)
fpiece=float(piece)
print(fpiece)