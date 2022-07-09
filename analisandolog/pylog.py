import sys

log = open('access.log','r')

## metodo que tira caracteres especiais
def takeOff(i):
    specialChars = ['[',']','(',')']
    for specialChar in specialChars:
       i = i.replace(specialChar,'')
    return i 

def ipCountRequest(log):
    lines = log.readlines()
    ipsSource = []
    ipsFoundNoRepeat = []
    for line in lines:
        ##quebrando a linha e jogando-a para uma lista 
        lineColumn = line.split(' ')

        ##Pegando o iP de cada requisição e jogando o mesmo para uma lista X para controle.
        for i in range(0,len(lineColumn[0])):
            ipsSource.append(lineColumn[0])

            ##Jogando o IP que ainda não apareceu e jogando o mesmo para outra lista Y para ter o controle dos IPs dentro do log.  
            if lineColumn[0] not in ipsFoundNoRepeat:
                ipsFoundNoRepeat.append(lineColumn[0])
            
    ##Consultando quantas vezes cada ip apareceu. Olha cada ip da lista Y (onde estão armezanados os IPs, sem repetir)
    ##e verificando quantas vezes o mesmo apareceu na lista X(Que salva o IP baseado nas requisições mesmo repetindo ou não)
    for ip in range(0,len(ipsFoundNoRepeat)):
        print(ipsFoundNoRepeat[ip] + ' - requests = ' + str(ipsSource.count(ipsFoundNoRepeat[ip])))

ipCountRequest(log)

