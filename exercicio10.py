lista = [2,4,7,2,3,3,1,0,2,6]

numero_mais_repetido = 0
qtd_repeticoes = 0

for numero in lista:
    qtd = lista.count(numero)
    if qtd > qtd_repeticoes:
        numero_mais_repetido = numero
        qtd_repeticoes = qtd

print("O número que se repete mais vezes é:", numero_mais_repetido)