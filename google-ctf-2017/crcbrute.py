import crccheck

message = 2417851639229258349412352

while message != crccheck.crc.Crc82Darc.calc(bytes(bin(message),"ascii")[2:]) :
	message += 1

#print(message)



