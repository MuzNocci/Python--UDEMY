velocidade = 70
pos_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

vel_RADAR_1 = velocidade > RADAR_1
pos_carro = pos_carro >= (LOCAL_1-RADAR_RANGE) and pos_carro <= (LOCAL_1+RADAR_RANGE)

if vel_RADAR_1:
    print('A velocidade do carro passou no RADAR 1.')

if pos_carro and vel_RADAR_1:
    print('O carro foi multado no RADAR 1.')
else:
    print('O NÃO foi multado no RADAR 1')
