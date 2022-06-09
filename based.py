##      PICOCTF  - based.py

##First Step:  Binary to String
def binToString(binValue):
    list_bin = binValue.split(' ')
    stringBin = ''
    for i in list_bin:
        stringBin += chr(int(i,2))
    return stringBin

##Secund Step:  Integer to String
def integerToString(integerValue):
    list_integer = integerValue.split(' ')
    stringInt = ''
    for j in  list_integer:
        #print(chr(int(j,8))) 
        stringInt += chr(int(j,8))
    return stringInt


##Third Step:  Hex to String
def hexToString(hexValue):
    return bytes.fromhex(hexValue).decode('utf-8')



binValue = input(str('Write the binary: '))
print(binToString(binValue))

integerValue = input(str('Write the integer sequence: '))
print(integerToString(integerValue))

hexValue = str(input('Write the hex value: '))
print(hexToString(hexValue))