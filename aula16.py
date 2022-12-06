"""
"""
#CONSTANTE = "Variáveis" que não vão mudar
#Muitas condições no mesmo if (ruim)
 #   <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega
verificar a velocidade do carro, a área de alcance do radar e aplicar ou não a multa.

em phyton as constantes são diferenciadas pela forma como são escritas
observe as variáveis abaixo, as constantes são as que estão escritas em maiusculo.

"""

##informações do carro

velocidade_carro = 61 # velocidade do carro no momento.
local_carro      = 99 # regiaõ em que o carro se encontra na estrada

RADAR_1     = 59 #VELOCIDADE PERMITIDA NO RADAR 1
LOCAL_1     = 100 # REGIÃO DA PISTA EM QUE O RADAR ESTÁ
RADAR_RANGE = 1 # ALCANCE DO RADAR.

if velocidade_carro > RADAR_1:
    print(f'{velocidade_carro}km está acima da velocidade permitida!')

if local_carro >=(LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade_carro > RADAR_1:
    print('carro multado')    