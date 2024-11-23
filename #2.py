'''
2. (Valor: 10 pontos) Faça um programa que solicite ao usuário um valor decimal positivo (esse valor
corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de
cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$
0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.
'''

saque   =  float ( input ('Informe o valor do saque = '))      

if saque <= 0:
    exit ('Digite um saque válido')
cedulas = 0

moedas  = 0

valordacedula = 100

valorentregue = round (saque, 2)

while True:
    if valordacedula <= valorentregue:
       cedulas += 1
       valorentregue -= round (valordacedula, 2)
    else:
        if cedulas >= 1 and valordacedula > 1:
            print (f'{cedulas} cédula(s) de R$ {valordacedula:.2f}')
        if cedulas >= 1 and valordacedula == 1:
            print (f'{cedulas} moeda(s) de R$ {valordacedula:.2f}')
        if  cedulas >= 1 and valordacedula < 1:
            print (f'{cedulas} moeda(s) de R$ {valordacedula:.2f} centavos')
        if valorentregue == 0:
            break
        if valordacedula == 100:
            valordacedula = 50
        elif valordacedula == 50:
            valordacedula = 20
        elif valordacedula == 20:
            valordacedula = 10 
        elif valordacedula == 10:
            valordacedula = 5
        elif valordacedula == 5:
            valordacedula = 2
        elif valordacedula == 2:
            valordacedula = 1
        elif valordacedula == 1:
            valordacedula = 0.50
        elif valordacedula == 0.50:
            valordacedula = 0.25
        elif valordacedula == 0.25:
            valordacedula = 0.10
        elif valordacedula == 0.10:
            valordacedula = 0.05 
        elif valordacedula == 0.05:
            valordacedula = 0.01
            break
        cedulas = 0




        


    
