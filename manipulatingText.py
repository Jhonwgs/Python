#Fatiamento de String é o termo que damos para a divisão de uma string em partes
frase="Programa para manipular texto"
print(frase)#exibindo a cadeira e caracter frase em tela.
print("O total de caracteres desta frase é:",len(frase))#toda string é um vetor com vários caracteres, verificando o tamanho do vetor frase
print(frase[9:13])#fatiamento em range, definido o inicio como 9 e o fim como 12 pois o 13 não entra.
print(frase[:29:3])#efetuando o fatiamento, pulando de 3 em 3 caracteres, onde quando o primeiro valor é omitido ele inicia do caracter zero
