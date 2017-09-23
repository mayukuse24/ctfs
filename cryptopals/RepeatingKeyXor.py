import binascii

K = "ICE"
msg = "abcdabcd"

def repeatedXor(message,key) :
    index = 0
    keybytes = bytes(key,"utf-8")
    result = b''
    for byte in bytes(message,"utf-8") :
        result += bytes([byte ^ keybytes[index%len(keybytes)]])
        index += 1

    return result

print(binascii.hexlify(repeatedXor(msg,K)))
    

