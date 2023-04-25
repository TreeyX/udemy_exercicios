nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'A primeira letra do seu nome é {nome[0]}.')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'A ultima letra do seu nome é {nome[-1]}.')
    print(f'Seu nome ao contrário é {nome[::-1]}.')
    print(f'Seu nome tem {len(nome)} Caracteres.')
    print(f'Voce tem {idade} anos de idade.')
else:
    print('Nome e idade são obrigatórios!')
    
