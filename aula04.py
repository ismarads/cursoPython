## Calculo IMC


# nome   = 'Ismar'
# idade  = 36
# altura = 1.75
# peso   = 82
# imc    = peso // altura ** 2

# abaixo_do_peso = imc < 18.5 
# acima_do_peso = imc > 25

# print(imc)
# print('está acima do peso?', abaixo_do_peso)
# print('está acima do peso?', acima_do_peso)

# print(nome ,'tem', idade, 'anos de idade', altura, 'de altura', 'está pesando', peso, 'kg', 'e seu IMC é:' ,imc)

#formatação de string f-strings

# texto_formatado = f'{nome} tem {idade} de idade e mede {altura} de altura e seu peso atual é {peso:.2f}kg e seu IMC é {imc}'

# print(texto_formatado)



# a ='A'
# b = 'B'
# c = 'C'
# string = 'a={} b={} c={}'
# formato = string.format(a, b, c)

# print(formato)


nome = 'Luiz'
idade = 23 
formato = '{n} tem {i} anos'

print(formato.format(n=nome, i=idade))