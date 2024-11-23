'''
Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo. 
Faça um programa que pergunta: o momento inicial da partida (hora e minuto), o momento de chegada 
(hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto 
(em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km);  
 
Após receber os dados, o programa informa dados típicos de um computador de bordo:  
 
a) o tempo de viagem (em segundos) 
b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h) 
c) o custo da viagem com combustível (em R$) 
d) o desempenho do carro (em Km/l, l/h e R$/Km). 
'''

#horas para segundos = * 3600 - minutos para segundos = / 3600
#horas para minutos ou minutos para segundos = * 60 - segundos para minutos ou minutos para horas = / 60

iniciodapartida = float ( input ('Informe o momento da partida no formato h/min = '))
chegada         = float ( input ('Informe o momento da chegada no formato h/min = '))
descansoemseg   = float ( input ('Informe os segundos parados para descanso = '))
combustivel     = float ( input ('O número de litros de combustível gasto = '))
preçocombust    = float ( input ('Informe o preço do combustível em R$ = '))
distancia       = float ( input ('Informe a distância percorrida em Km = '))

tempviagem = round ((chegada - iniciodapartida) * 3600)


print (f'{tempviagem}')

