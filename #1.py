'''
1. (Valor: 10 pontos) Faça um programa que aceita um número de até 4 dígitos (0 a 9999) e exiba a soma 
dos seus algarismos.
'''


n       = int ( input ('Informe um número de até 4 digítos = '))

if n < 0:
    exit ('Informe um número positivo')
elif n > 9999:
    exit ('Informe um número de até 4 digítos')
# M = Milhar, C = Centena, D = Dezena e U = Unidade.

m       = n // 1000

resto_m = n % 1000

c       = resto_m // 100

resto_c = resto_m % 100

d       = resto_c // 10

u       = resto_c % 10

soma    = m + c + d + u

print (f'A soma dos algarismos é = {soma}')



