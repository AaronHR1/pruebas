def binaryDecimal(binario):
    binario=str(binario)
    numero=0
    exponente=0
    for i in range(len(binario),0,-1):
        num=int(binario[i-1])
        numero+=num*2**exponente
        exponente+=1
        print(num)
    print(numero)


def decimalBinary(decimal):
    exponente=0
    while 2**exponente<=decimal:
        exponente+=1
    exponente-=1
    binario=""
    while exponente>=0:
        
        if 2**exponente>decimal:
            binario+="0"
        else:
            binario+="1"
            decimal=decimal-2**exponente
        
        exponente-=1
    
    return binario


print(decimalBinary(2))