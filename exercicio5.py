contador = 0
listP = []
listI = []
somaP = 0
somaI = 0
while  contador < 10:
    num = int(input("Digite um número: "))
    contador += 1
    if num % 2 != 0:
        listI.append(num)
        somaP += 1
    elif num % 2 != 1:
        listP.append(num)
        somaI += 1

print (f"Os números Pares são{listP} no total foram {somaP} números Pares")
print (f"Os números Impares são{listI} no total foram {somaI} números Impares")