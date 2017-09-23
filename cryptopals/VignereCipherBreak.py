from operator import itemgetter
import base64

alphamap = "abcdefghijklmnopqrstuvwxyz 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'"

cipher = base64.b64decode(open("6.txt").read()) #bytearray form of base64 cipher

def hammingDistance(bytearr1,bytearr2) :
    total = 0
    for byte1,byte2 in zip(bytearr1,bytearr2) :
        total += bin(byte1 ^ byte2).count('1')

    return total


def avgHammingDistance(bytearr1,keylen) :
    if len(bytearr1) < 2*keylen :
        assert("input bytearray too small to calculate average hamming distance")
    reslist = []
    for i in range(0,len(bytearr1),keylen) : 
        reslist.append(hammingDistance(bytearr1[i:i+keylen],bytearr1[i+keylen:i+2*keylen])/keylen) #Normalized HD

    return sum(reslist)/len(reslist) #average

def strScore(bytearr) :
    count = 0
    for char in bytearr :
        if char in bytes(alphamap,"ascii") :
            count += 1

    return count/len(bytearr)

def mostLikelyKeyChar(bytearr) :
    scorelist = []
    for i in range(256) :
        out = b''
        for char in bytearr :
            out += bytes([char ^ i])
        scorelist.append((i,strScore(out)))
        
    return bytes([sorted(scorelist,key=itemgetter(1),reverse=True)[0][0]])
    
def bruteKey(cipher,keylength) :
    out = b''
    for index in range(keylength) :
        testarr = [cipher[x] for x in range(index,len(cipher),keylength)]
        out += mostLikelyKeyChar(testarr)

    return out

def repeatedXor(message,key) :
    index = 0
    result = b''
    for byte in message :
        result += bytes([byte ^ key[index%len(key)]])
        index += 1

    return result

def vignereBreak(cipher) :
    hamdistlist = []
    for i in range(2,40) :
        hamdistlist.append((i,avgHammingDistance(cipher,i)))
    
    hamdistlist = sorted(hamdistlist,key=itemgetter(1))
    
    keylist = [x[0] for x in hamdistlist]

    for key in keylist[0:5] : #Select top 5 likely key lengths
        print("Testing for key length",key)
        bytekey = bruteKey(cipher,key)
        print(bytekey,key)
        print("Possible Decrypted message from key",repeatedXor(cipher,bytekey))

print(vignereBreak(cipher))
    
