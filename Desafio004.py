print('====== DESAFIO 04 =====')
p = input('Digite Qualquer Coisa : ')
print('Você digitou {}'.format(p))
print('é do tipo {}'.format(type(p)))
print('É numerico?', p.isalnum())
print('É Alfalnumerico?', p.isalpha())
print('É decimal ?', p.isdecimal())
print('Caso seja string esta em maisculo?', p.isupper())
print('É umd digito ?', p.isdigit())
print('É indentificavel ?', p.isidentifier())
print('Caso seja string, esta em minusculo ?', p.islower())
print('É uma tabela ?', p.isprintable())
print('É um espaço ?', p.isspace())
print('Esta Capitalizada (maiuscula e minuscula) ?', p.istitle())
