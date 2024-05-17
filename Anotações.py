#Tipos de Dados

# -> STR: “Meu nome é Matt”  “10”
# -> FLOAT: 10.5  -5.2  6000.0001
# -> BOOL: True False

# -------------Entrada de dados--------------

# -> INPUT( ): Pode escrever dentro do parênteses ao invés de criar um PRINT antes do INPUT

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

# int() para inteiros
# float() para números flutuantes como salários, número com virgula, etc
# str() strings, textos, etc
