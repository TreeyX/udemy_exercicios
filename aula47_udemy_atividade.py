nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade != False:
    print(f'Seu nome é {nome}.')
    print(f'A primeira letra do seu nome é {nome[1]}.')
    print(f'A ultima letra do seu nome é {nome[-1]}.')
    print(f'Seu nome ao contrário é {nome[-1:-(len(nome)+1):-1]}.')
    print(f'Seu nome tem {len(nome)} Caracteres.')
    print(f'Voce tem {idade} anos de idade.')
else:
    print('Nome e sua idade são obrigatórios!')
