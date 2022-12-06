#Introdução ao try/except
#try ->  tentar executar o código
#except -> ocorreu algum erro ao tentar executar
numero_str = input('vou dobra o valor digitado ')

try:
    nummero_float = float(numero_str)
    print('float:', nummero_float)
    print(f'o dobro de  {numero_str} é {nummero_float *2:.2f}')
except:
    print('Isso não é um número')    