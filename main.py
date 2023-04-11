anoA = int(input('Qual o ano atual? : '))
idade = int(input('Qual a sua idade? : '))
ano2 = int(input('Digite outro ano: '))
nome = str(input('Qual o seu nome? : '))
novaidade = (ano2 - anoA) + idade 
print('{}, no ano de {} você terá {} anos'.format(nome, ano2, novaidade))