nome = str(input('Qual é o seu nome? '))
if nome == 'luiz':
    print('Que nome bonito !')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seus nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome).title())
