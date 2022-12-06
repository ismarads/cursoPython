#praticando if

##calculo de média

av1 = input('digite a nota da sua primeira avaliação: ')
av2 = input('digite a nota da sua segunda avaliação: ')
av3 = input('digite a nota da sua terceira avaliação: ')

nota1 = int(av1)
nota2 = int(av2)
nota3 = int(av3)


media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'Parabéns, você foi aprovado com média {media}')
elif media <= 6.9:
    print(f'Que pena, não foi dessa vez. tente de novo. sua média foi {media}')
# else:    