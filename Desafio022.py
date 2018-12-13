
print(' ===  Desafio 022  ===\n')
print('Analisando um Texto\n\n')
      
print("""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.\n\n""")

nome = str(input('Digite seu nome completo: ')).strip()
# strip() retira os espaços finais e iniciais

print('Analisando seu nome....\n')
print('Seu nome em letras maisculas Ficara assim : {}'.format(nome.upper()))

print('Seu nome em letras minusculas Ficara assim : {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
