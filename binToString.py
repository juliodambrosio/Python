import sys

if len(sys.argv) > 1:
    str_bin = ''
    for i in range(1,len(sys.argv)):
        bin = sys.argv[i]
        lista_bin = bin.split(' ')
        for j in lista_bin:
            str_bin += chr(int(j,2))
    print(str_bin)
else:
    print('O script necessita de um argumento')
    print('Exemplo: ')
    print('./binToString.py 10101010 01010101 01101010101')