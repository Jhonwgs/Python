#Programa para ler 2 valores inteiros e armazenar em variaveis e efetuar a soma dos 2 números

A, B = map(int, input().split())
#RECEBENDO VIA TECLADO O VALOR DAS VARIAVEIS A & B
#Através da função map, estamos transformando o dado recebido do
# teclado que se torna uma string em um dado capaz de fazer calculo, neste caso inteiro

X = A + B
#Atribuindo o valor de A & B na variavel X e efetuando a soma dos 2 valores

print('x = ',X)
#Exibindo na tela o valor da soma