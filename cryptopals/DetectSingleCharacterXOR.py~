import SingleByteXorCipher as blib
from operator import itemgetter

bestofbest = []
with open("4.txt",'r') as fread :
    for line in fread.read().splitlines() :
        bestofbest += sorted(blib.bruteByte(line),key=itemgetter(1), reverse=True)[0:1]

print(sorted(bestofbest,key=itemgetter(1),reverse=True)[0:5])
