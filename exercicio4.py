lista = []
soma = 0
while True:
    idade = int(input("Idades, 0 para sair: "))
    if idade == 0:
        break
    else:
        lista.append(idade)
        soma += idade
        

media = soma/len(lista)

print(f"A média das idades é {media}")
