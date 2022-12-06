"""
exercício

peça ao usuário para digitar seu nome
peça ao usuára para digitar sua idade

se o nome e idade forem digitados exiba
seu nome é {nome}
seu nome invertido é {nome invertido}
seu nome contem  (ou não ) espaços
seu nome tem {n} letras
a primeira letra do seu nome é {letra}
a ultima letra do seu nome é {ultima letra}
se nada for digitado em nome e idade
exiba: "Desculpe, você deixou campos vazios"
"""

campo_nome  = input("Digite seu nome: ")
campo_idade = input("Digite sua idade: ")

#usr_name = campo_nome
#usr_age = int(campo_idade)

if campo_nome and campo_idade:
    print(f'seu nome é {campo_nome}')
    print(f'Seu nome invertido é {campo_nome[::-1]}')
    if ' ' in campo_nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não cotém espaços')    
    print(f'Seu nome contém {len (campo_nome)} letras')
    print(f'A primeira letra do seu nome é "{campo_nome[0]}"')
    print(f'Aultima letra do seu nome é "{campo_nome[-1]}"')
else:
    print("Você deixou um campo em branco")