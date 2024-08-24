#Código utilizando a biblítoteca random para gerar um número aleatório correspondente a um aluno em uma lista
import random
from random import randint
alunos = list()#gerando uma lista vazia que receberá o nome de 4 alunos
alunos.append(input("Informe o nome do primeiro aluno: "))#solicitando ao usuario o nome do primeiro aluno
alunos.append(input("Informe o nome do segundo aluno: "))#solicitando ao usuario o nome do segundo aluno
alunos.append(input("Informe o nome do terceiro aluno: "))#solicitando ao usuario o nome do terceiro aluno
alunos.append(input("Informe o nome do quarto aluno: "))#solicitndo ao usuario o nome do quarto aluno
sorteado = random.choice(alunos)#sorteando um elemento aleatório dentro do range de posições do vetor alunos para escolher 1 aluno
print("O aluno(a) escolhido foi ",sorteado)#exiindo em tela o aluno sorteado