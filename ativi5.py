def somaImposto(taxa = 0, custo = 0):
    total = custo * (taxa/100 + 1)
    return print(f'O custo total do produto com imposto será de R${total}')

taxa = float(input('Informe a taxa de imposto para alterar o preço do produto: '))
custo = float(input('Inform o preço do produto: R$'))
somaImposto(taxa, custo)