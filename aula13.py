""" fatimante de strings
numeros negativos também são posições
 """


descricao_material = 'polietileno tereftalato'
print(descricao_material[0:5]) #informando o zero quer dizer que traremos a partir da primeira posição
print(descricao_material[3:6]) # dessa forma será exibido a partir da 3ª posição até a 5ª posição, isso mesmo 5ª posição
print(descricao_material[6:])  # dessa forma será exibido a partir da 6ª posição até a ultima posição
print(descricao_material[:23]) # dessa forma será exibido a partir da 1ª posição até a posição 23, que no caso é a ultima 
print(len(descricao_material)) # len conta o tamanho da variável(obs.: a contagem de caracteres é diferente de índice d)
print(len(descricao_material[3:9])) # aqui pega a quantidade solicitada.
print(descricao_material[0:23:3]) # o 0 quer dizer a partir do primeiro, o 23 o total de caracteres da variavel e o 3 é quantidade de passos, ou seja, de 3 em 3 
print(descricao_material[::-1]) # inverto a ordem, o que resultará na string escrita de trás para frente 