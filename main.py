nome = str(input('Qual o seu nome? : '))
anoA = int(input('Qual o ano atual? : '))
idade = int(input('Qual a sua idade? : '))
ano2 = int(input('Digite outro ano: '))
novaidade = (ano2 - anoA) + idade 
print('{}, no ano de {} você terá {} anos'.format(nome, ano2, novaidade))