
print(' ===  Desafio 034  ===\n')


print('         Aumentos múltiplos \n\n')
"""
  Escreva um programa que pergunte o salário de um funcionário e
  calcule o valor do seu aumento.
  Para salários superiores a R$1250,00, calcule um aumento de 10%.
  Para os inferiores ou iguais, o aumento é de 15%.

"""
salario = float(input('Digite o seu salario: '))

if salario < 1250.00:
    print('Você ganhou 15% de aumento, seu novo salario é de R$ {:.2f}'.format(salario * 15 / 100 + salario))
else:
    print('Você ganhou 10% de aumento, seu novo salario é de R$ {:.2f}'.format(salario * 10 / 100 + salario))
    
