#Tipos de Dados

# -> STR: “Meu nome é Matt”  “10”
# -> FLOAT: 10.5  -5.2  6000.0001
# -> BOOL: True False

# -------------Entrada de dados--------------

# -> INPUT( ): Pode escrever dentro do parênteses ao invés de criar um PRINT antes do INPUT.

# -------------Saída de dados----------------

# -> PRINT( ): Para chamar variaveis num PRINT, adicione um “f” dentro da parênteses e abra as chaves na variável.
# Ex:
   print(f"Olá {nome}, sua idade é {idade}")

# ------------Conversão de dados-------------

# Em um exemplo onde você precisaria definir as notas de um aluno, você terá que definir antes o tipo de dado que você precisa, por exemplo:

nota1 = input('Digite sua nota: ')
nota2 = input('Digite sua nota 2: ')

# Nesse exemplo, quando o usuário digitar as notas, elas serão impressas com tipo STRINGS, então se você usar PRINT(NOTA1 + NOTA2), a maquina só irá colocar as duas notas juntas, tipo “1010” justamente por achar que é uma STRING.

# Pra consertar isso, você definirá o tipo de dado:

nota1 = input('Digite sua nota: ')
nota2 = input('Digite sua nota 2: ')

nota1 = float(nota1)
nota2 = float(nota2)
#       OU
nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota 2: '))
# int() para inteiros.
# float() para números flutuantes como salários, número com virgula, etc.
# str() strings, textos, etc.

# -----------Operadores aritméticos [+ - /  //  %   *   **]--------------

# ‘ / ‘ serve para divisão, porém o ‘ // ‘ também serve para o mesmo, mas, ele sempre irá devolver o número como inteiro. Qualquer divisão que devolveria como 3,3333… 2,5 e etc, o // irá devolver como 3, 2 e etc.
# ‘ % ‘ é o módulo, irá mostrar o resto da divisão **(não entendi muito bem, pesquisar).
# ‘ ** ‘ representa o número elevado, e serve pra fazer uma raiz quadrada elevando a meio (1/2).

# ------------Operadores Relacionais [>  <  =  ==  !=]----------------

# = Atribuição de valor.
# == Comparação entre dois valores.

# ------------Operadores Lógicos [and or not]--------------

# Basicamente é tabela da verdade do e ( ^ ) & do ou ( < )

# -----------Estrutura de decisão [if, else, elif ]--------------

# Em python, não precisa utilizar chaves, você utiliza um espaço TAB para deixar o argumento dentro do IF.

# -----------Laço de repetição WHILE-------------
i = 1
while i <= 5:
print( i )
i = i + 1
# Ou pode usar o incremento +=
# i começa valendo 1, então o WHILE define que enquanto i for menor ou igual a 5, imprima i, e após isso ele define novamente o i como i + 1, no caso, 1 + 1, e repete o processo com o i tendo esse novo valor até ele chegar a 5

# BREAK quebra o laço de repetição, por exemplo:
while True:
	nota_aluno = int(input('Digite a nota do aluno: '))
	
	if nota_aluno >= 0 and nota_aluno <= 10:
		break
		
	print('Fui encerrado')
# após o BREAK quebrar a repetição, a maquina para de ler essa estrutura do WHILE e lê o PRINT.

# -----------Laço de repetição FOR------------

for i in range(1, 11):
	print(i)
#o RANGE define onde o FOR começa e onde ele termina, no caso desse exemplo, ele irá até o número 10 pois o último número sempre será -1, então se você querer os números de 1 a 10 = RANGE(1, 11). de 1 a 11 = RANGE(1, 12). etc

# Pra mostrar os valores pares de 1 a 1000
for i in range(1, 11):
	if i % 2 == 0
		print(i)
# Se a divisão por 2 de i tiver resto igual a 0, então ele é par.

# Aqui  está sendo implementado impressão de números sendo adicionados de 2 em 2.
# Começa do 2, até o 10, de 2 em dois.
for i in range(2, 11, 2): 
	print(i)
# 2, 4, 6, 8, 10
# mesma coisa pra subtração

# Tabuada do 2 até o 100
for i in range(1, 101):
	print(f'{2} x {i} = {2 * i}')

# Tabuada do 1 ao 5 até o 10 **FOR dentro de FOR**
for i in range(1, 6):
	for j in range(1, 11):
		print(f'{i} x {j} = {i*j}')
	print('=========================')
   
# -----------Listas-------------

# Listas lembram bastante um vetor ou array (eu acho), elas vão armazenar valores e poderá ser acessada pela posição dos mesmos. Exemplo:
medias_alunos = [10, 20, 5, 4, -2]
					 # 0,  1, 2, 3,  4
print(medias_alunos[0])

# Aqui o for irá passar por cada um desses valores
medias_alunos = [10, 20, 5, 4, -2]
					 # 0,  1, 2, 3,  4
for i in medias_alunos:
print('O valor atual é {i}')
# O valor atual é 10
# O valor atual é 20
# O valor atual é 5
# etc

# Você pode adicionar valores a lista também:
medias_alunos = [10, 20, 5, 4, -2]
					 # 0,  1, 2, 3,  4
print(media_alunos)

medias_alunos.append(60)

print(media_alunos)
# [10, 20, 5, 4, -2, 60]

# Aqui é um código para um professor adicionar notas numa lista
medias_alunos = [] #Lista vazia
while True:
	nota = int(input('Digite uma nota ou -1 para sair: '))
	if nota == -1:]
		break
		
	medias_alunos.append(nota)
	print(medias_alunos)
	
	#Agora adicionando a soma pra média
	soma = 0
	quantidade = 0
	for i in medias_alunos:
		soma = soma + i
		quantidade = quantidade + 1
	
	print(soma/quantidade)
	#10
	#10
	#-1
	#Resultado: 10
# **Só não entendi muito bem pq a divisão dos dois acabou dando 10 também**

# --------------Dicionáarios------------------

# Um dicionário é uma estrutura onde você armaezena uma chave e um valor, por exemplo:
pessoas = {’nome’: ‘pedro’, ‘idade’: 55, ‘altura’: 178}
		  	  #key,    value,   key,  value,  key,   value

print(pessoas['idade']) #specificando uma key
print(pessoas.keys())   #especificando todos as keys
print(pessoas.values()) #especificando todos os values

#Para adicionar mais uma key, basta apenas:
pessoas['cep'] = '40028922'

# -----------------Funções------------------

# Basicamente serve pra repetir um bloco de código sem ter que sempre refazer o mesmo
def calcula_media(): #Definindo a função
	print('Estou')
	print('Aqui')
	
calcula_media()      #Chamando a função
#Estou
#Aqui
------------------------
def calcula_media(n1, n2): #Definindo a função
	print((n1 + n2)/2)
	
calcula_media(10, 10)
calcula_media(10, 5)
#10
#5

# --------------Modularização/Importações------------------

# Separa o código em pequenos trechos de código para se ter um controle maior.
# Em um arquivo chamado Calculos temos:
def calcula_media(n1, n2):
	print((n1 + n2)/2)
	
PI = 3.14

# Já em outro arquivo chamado App:
# Apenas irá chamar o que foi definido no Calculos
import calculos # Aqui ele importa o arquivo para que as funções, variaveis e etc de outros aqrquivos possam ser usadas.
calculos.calcula_media(10, 10)
print(calculos.PI)

#       ou

from calculos import calcula_media
calcula_media(10, 10)
print(PI) #Não funcionaria nesse modelo porque o import está definindo que irá só importar a função calcula_media e mais nada. a menos que você adicione o PI após o calcula_media no import.
