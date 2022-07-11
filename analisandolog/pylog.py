from pickletools import read_int4
import sys

from requests import request


## metodo que tira caracteres especiais
def takeOff(i):
    specialChars = ['[',']','(',')',' ']
    for specialChar in specialChars:
       i = i.replace(specialChar,'')
    return i 
## Metodo que mostra quantas requisiçoes houveram por IP
def ipCountRequest(log):
    lines = log.readlines()
    ipsSource = []
    ipsFoundNoRepeat = []
    for line in lines:
        ##quebrando a linha e dividindo o conteúdo entre espaços 
        lineColumn = line.split(' ')

        ##Pegando o iP de cada requisição e jogando o mesmo para uma lista X para controle.
        for i in range(0,len(lineColumn[0])):
            ipsSource.append(lineColumn[0])

            ##Jogando o IP que ainda não apareceu e jogando o mesmo para outra lista Y para ter o controle dos IPs dentro do log.  
            if lineColumn[0] not in ipsFoundNoRepeat:
                ipsFoundNoRepeat.append(lineColumn[0])
            
    ##Consultando quantas vezes cada ip apareceu. Olha cada ip da lista Y (onde estão armezanados os IPs, sem repetir)
    ##e verificando quantas vezes o mesmo apareceu na lista X(Que salva o IP baseado nas requisições mesmo repetindo ou não)
    print('--------TOTAL REQUESTS--------')
    ipsFoundNoRepeat.sort()
    for ip in range(0,len(ipsFoundNoRepeat)):
        print(ipsFoundNoRepeat[ip] + ' = ' + str(ipsSource.count(ipsFoundNoRepeat[ip])))
## Metodo que mostra requisiçoes feita que ocorreram em uma data
def requestPerDay(log):
    lines = log.readlines()
    data = '11/Feb/2015'
    for line in lines:
        line = line.split(' ')
        # print(line)
        # print(line[3])
        
        datalog = line[3][1:12]
        if data == datalog:
            print(line,end=' ')
            print()
    

log = open('access.log','r')

#ipCountRequest(log)
requestPerDay(log)

log.close()