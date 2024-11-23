'''
2. (Valor: 10 pontos) Faça um programa que solicite ao usuário um valor decimal positivo (esse valor
corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de
cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$
0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.
'''

saque   =  float ( input ('Informe o valor do saque = '))      

cedulas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas  = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
if saque <= 0:
    exit ('Informe um saque válido')
else:
    cemR = round (saque, 2) // 100
    saque = round (saque, 2) % 100
  
    cinquentaR = round (saque, 2) // 50
    saque = round (saque, 2) % 50

    vinteR = round (saque, 2) // 20
    saque = round (saque, 2) % 20

    dezR = round (saque, 2) // 10
    saque = round (saque, 2) % 10

    cincoR = round (saque, 2) // 5
    saque = round (saque, 2) % 5

    doisR = round (saque, 2) // 2
    saque = round (saque, 2) % 2

    umR = round (saque, 2) // 1
    saque = round (saque, 2) % 1

    cinquentaC = round (saque, 2) // 0.5
    saque = round (saque, 2) % 0.5

    vintecincoC = round (saque, 2) // 0.25
    saque = round (saque, 2) % 0.25

    dezC = round (saque, 2) // 0.10
    saque = round (saque, 2) % 0.10

    cincoC = round (saque, 2) // 0.05
    saque = round (saque, 2) % 0.05
   
    umC = round (saque, 2) / 0.01
    
    
if cemR >= 1:
    print (f'{cemR:.0f} cédula(s) de R$ {cedulas[0]:.2f}')
if cinquentaR >= 1:
    print (f'{cinquentaR:.0f} cédula(s) de R$ {cedulas[1]:.2f}')
if vinteR >= 1:
    print (f'{vinteR:.0f} cédula(s) de R$ {cedulas[2]:.2f}')
if dezR >= 1:
    print (f'{dezR:.0f} cédula(s) de R$ {cedulas[3]:.2f}')
if cincoR >= 1:
    print (f'{cincoR:.0f} cédula(s) de R$ {cedulas[4]:.2f}')
if doisR >= 1:
    print (f'{doisR:.0f} cédula(s) de R$ {cedulas[5]:.2f}')
if umR >= 1:
    print (f'{umR:.0f} moeda(s) de R$ {moedas[0]:.2f}')
if cinquentaC >= 1:
    print (f'{cinquentaC:.0f} moeda(s) de R$ {moedas[1]:.2f}')
if vintecincoC >= 1:
    print (f'{vintecincoC:.0f} moeda(s) de R$ {moedas[2]}')
if dezC >= 1:
    print (f'{dezC:.0f} moeda(s) de R$ {moedas[3]:.2f}')
if cincoC >= 1:
    print (f'{cincoC:.0f} moeda(s) de R$ {moedas[4]}')
if umC >= 1:
    print (f'{umC:.0f} moeda(s) de R$ {moedas[5]}')


