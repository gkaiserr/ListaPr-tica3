intervalo = 0
cont = 0
for i in range(0,10):
    num = int(input("num: "))
    if num  < 10 or num > 20:
        intervalo +=1
    else:
        cont += 1

print (f"{cont} números estão no intervalo de 10 - 20")
print (f"{intervalo} números não estão no intervalo de 10 - 20")