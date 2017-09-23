import binascii

alphamap = "abcdefghijklmnopqrstuvwxyz 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'"

def bruteByte(hexstr) :
    inputstr = binascii.unhexlify(hexstr)
    scorelist = []
    for i in range(256) :
        out = b''
        for char in list(inputstr) :
            out += bytes([char ^ i])
        scorelist.append((out,strScore(out),hexstr))
    return scorelist

def strScore(bytearr) :
    count = 0
    for char in bytearr :
        if char in bytes(alphamap,"ascii") :
            count += 1

    return count/len(bytearr)

