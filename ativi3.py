def soma_tres_nums(num1 = 0, num2 = 0, num3 = 0):
    soma = num1 + num2 + num3
    return print(f'A somas dos números {num1}, {num2} e {num3} é igual a {soma}.')

num1 = int(input('Informe o primeiro valor para a soma: '))
num2 = int(input('Informe o segundo valor para a soma: '))
num3 = int(input('Informe o terceiro valor para a soma: '))

soma_tres_nums(num1, num2, num3)
