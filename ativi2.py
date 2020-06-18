def funcao_numero(num = 0):
    ultimo = num
    primeiro = 1
    while True:
        for c in range(1,primeiro + 1):
            print(f'{c} ',end=' ')
        print()
        primeiro += 1
        if primeiro > ultimo:
            break

num = int(input('Informe um número para ver uma tabela personaliada: '))
funcao_numero(num)