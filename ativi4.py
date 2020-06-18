def positivo_ou_negativo(num = 0):
    return 'N' if num <=0 else 'P'

num = int(input('Informe um valor: '))
print(positivo_ou_negativo(num))