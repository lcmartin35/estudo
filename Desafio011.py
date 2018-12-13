print(' ===  Desafio 011  ===')
 
"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 
 
"""
print('     Cauculador de tinta')

altura = float(input('Digite a altura da parede :'))
largura = float(input('Digite a largura da parede :'))

m2 = altura * largura
litro = 2
print('A parede possui {:.2f} metros quadrados\n'.format(m2))
print('Serão necessarios {:.2f} litros para pintar a parede'.format(m2 / litro))
 
