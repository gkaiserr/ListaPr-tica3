while True:
    num = int(input("Digite num"))
    if num < 1 or num > 10:
        print("ERRO")
        continue
    else:
        for i in range(1,11):
            print(i*num)
