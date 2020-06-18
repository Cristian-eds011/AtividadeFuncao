def funcao_numero(num = 0):
    ultimo = num
    while True:
        for c in range(1,ultimo + 1):
            print(f'{c} '* c)
        print()
        break

num = int(input('Informe um número para ver uma tabela personolizada: '))
funcao_numero(num)