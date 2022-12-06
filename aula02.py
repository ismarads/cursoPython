## a função print recebe parametros separado por virgulas bem como operações matemáticas
##para  caracteres/string basta colocar entre aspas
# o argumento sep='' pode ser usado com aspas simples ou dupla
print('Joao')
print(56 ,'anos', 'Pai de Bruna')
print('casado com Helena',)
print('Analista de sistemas', 'Certificado Microsift')


### vamos para os tipos de dados
#tipagem dinâmica e forte
#str -> string -> texto
# string vem dentro de aspas


# aspas simples
print('Joao')
#as pas duplas
print("mesmo resultado")
#escap
print("coletivo de peixe é \"cardume\"") ## o escape, no caso a barra, faz o interpretador iginorar o que vem colado com ela.
print(r"coletivo de peixe é \"cardume\"") ## o r é utilizado para expressões regulares e acaba tornando visível as barras.
print('Python')

print(type(1000)) ### a 'função' q na verdade é uma classe ela exibe o tipo de dado

print(10==10)## tipo bool de sinal 
print(10==11)## dois sinais de igual seguidos é comparação.
print(int('2')+ 5) ### convertendo strg em int
print(float('5')+ 8) #convertendo em floats