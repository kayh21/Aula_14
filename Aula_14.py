# MÉTODO POP COM LISTAS E DICIONÁRIOS:

# O método `pop()` em Python é usado para remover um elemento de uma lista (ou um item de um dicionário) com base no índice especificado. 
# O método `pop()` retorna o valor do elemento removido. Aqui está a sintaxe básica do método `pop()`:
# lista.pop(indice)

# onde:
# `lista` é a lista da qual você deseja remover um elemento.
# `indice` é o índice do elemento que você deseja remover.
# Vamos ver um exemplo de uso do método `pop()` com uma lista:
frutas = ["maçã", "banana", "laranja", "uva"]
fruta_removida = frutas.pop(1)  # Remove o elemento com índice 1 (banana)
print(frutas)  # A lista agora é ["maçã", "laranja", "uva"]
print("Fruta removida:", fruta_removida)  # Isso imprimirá "Fruta removida: banana"

# Observe que o índice especificado deve estar dentro dos limites da lista. Se o índice estiver fora dos limites, você receberá um erro `IndexError`. Se você não especificar 
# um índice, `pop()` removerá o último elemento da lista por padrão. Além disso, você também pode usar o método `pop()` com dicionários para remover um item com uma chave 
# específica:
dicionario = {"chave1": "valor1", "chave2": "valor2", "chave3": "valor3"}
item_removido = dicionario.pop("chave2")  # Remove o item com chave "chave2"
print(dicionario)  # O dicionário agora é {"chave1": "valor1", "chave3": "valor3"}
print("Item removido:", item_removido)  # Isso imprimirá "Item removido: valor2"

# Ao usar o método pop() com dicionários, é importante especificar a chave que deseja remover.

# MÉTODO JOIN EM PYTHON:
# O método join() em Python é usado para concatenar elementos de uma sequência (geralmente uma lista) em uma única string. 
# Ele é chamado em uma string que atua como um "separador" e recebe uma sequência como argumento. O método join() cria uma nova string onde os elementos
# da sequência são separados pelo separador especificado. Aqui está a sintaxe básica do método join():
# separador.join(sequencia)
# string.join(iterable)

# onde: separador é a string que será usada para separar os elementos da sequência. sequencia é a sequência da qual você deseja concatenar os elementos em uma única string.
# Aqui está um exemplo de uso do método join() com uma lista:
palavras = ["Olá", "mundo", "em", "Python"]
frase = " ".join(palavras)  # Concatena os elementos da lista com um espaço em branco entre eles
print(frase)  # Isso imprimirá "Olá mundo em Python"

# No exemplo acima, o método join(" ") concatena os elementos da lista palavras em uma única string, separando-os com um espaço em branco.
# Você pode usar qualquer string como separador. Por exemplo:
numeros = ["1", "2", "3", "4", "5"]
csv = ",".join(numeros)  

# Concatena os elementos da lista com vírgulas entre eles
print(csv)  # Isso imprimirá "1,2,3,4,5"

# O método join() é muito útil quando você precisa construir strings a partir de elementos em uma sequência, economizando tempo e tornando o código mais legível.

# INDEXAÇÃO EM PYTHON:
# Em Python, a indexação usando : em uma sequência, como uma string, lista ou tupla, é usada para criar fatias (slices) dessa sequência. A notação geral é [começo:fim],
# onde:
# começo: O índice onde a fatia começa (inclusive).
# fim: O índice onde a fatia termina (exclusivo).
# Se você omitir começo, a fatia começará do início da sequência. Se você omitir fim, a fatia irá até o final da sequência. Veja alguns exemplos:
minha_string = "Olá, Mundo!"

# Obtém os primeiros 5 caracteres da string
parte1 = minha_string[:5]  # "Olá, "

# Obtém os caracteres da posição 7 até o final da string
parte2 = minha_string[7:]  # " Mundo!"

# Obtém os caracteres da posição 2 até a posição 4 (exclusivo)
parte3 = minha_string[2:4]  # "á,"

# Obtém todos os caracteres da string (equivalente a não especificar começo e fim)
toda_string = minha_string[:]  # "Olá, Mundo!"

# Você também pode usar índices negativos para contar a partir do final da sequência
final_da_string = minha_string[-6:]  # "Mundo!"

# Note que a indexação com : é muito flexível e pode ser usada em uma variedade de sequências em Python, como strings, listas e tuplas, para criar fatias das mesmas.
numero = "numero "
parte_da_string = numero[4:]

# Isso criará uma nova variável chamada parte_da_string que conterá os caracteres da string original "numero " a partir da quinta posição em diante, ou seja, "ro ".
# Aqui está o código corrigido:
numero = "numero "
parte_da_string = numero[4:]
print(parte_da_string)  # Isso imprimirá "ro "

# Lembre-se de que a indexação em Python começa em 0, então numero[4] retorna o quarto caractere da string original, que é "e". A partir do quinto caractere em diante 
# é obtido usando numero[4:].

# Exercício 1: Remova o último elemento de uma lista e imprima a lista resultante.
lista = [1, 2, 3, 4, 5]
lista.pop(4)
print(lista)

# Exercício 2: Remova o elemento de índice 2 de uma lista e imprima a lista resultante
lista = [10, 20, 30, 40, 50]
lista.pop(2)
print(lista)

# Exercício 3: Remova o primeiro elemento de uma lista e o último elemento usando pop() e imprima a lista resultante.
lista = [1, 2, 3, 4, 5]
lista.pop ()
print(lista)


# MÉTODOS 
# capitalize(): #Converts the first character to upper case
# casefold(): #Converts string into lower case
# center(): #Returns a centered string
# count(): #Returns the number of times a specified value occurs in a string
# encode(): #Returns an encoded version of the string
# endswith(): #Returns true if the string ends with the specified value
# expandtabs(): #Sets the tab size of the string
# find(): #Searches the string for a specified value and returns the position of where it was found
# format(): #Formats specified values in a string
# format_map(): #Formats specified values in a string
# index(): #Searches the string for a specified value and returns the position of where it was found
# isalnum(): #Returns True if all characters in the string are alphanumeric
# isalpha(): #Returns True if all characters in the string are in the alphabet
# isascii(): #Returns True if all characters in the string are ascii characters
# isdecimal(): #Returns True if all characters in the string are decimals
# isdigit(): #Returns True if all characters in the string are digits
# isidentifier(): #Returns True if the string is an identifier
# islower(): #Returns True if all characters in the string are lower case
# isnumeric(): #Returns True if all characters in the string are numeric
# isprintable(): #Returns True if all characters in the string are printable
# isspace(): #Returns True if all characters in the string are whitespaces
# istitle(): #Returns True if the string follows the rules of a title
# isupper(): #Returns True if all characters in the string are upper case
# join(): #Converts the elements of an iterable into a string
# ljust(): #Returns a left justified version of the string
# lower(): #Converts a string into lower case
# lstrip(): #Returns a left trim version of the string
# maketrans(): #Returns a translation table to be used in translations
# partition(): #Returns a tuple where the string is parted into three parts
# replace(): #Returns a string where a specified value is replaced with a specified value
# rfind(): #Searches the string for a specified value and returns the last position of where it was found
# rindex(): #Searches the string for a specified value and returns the last position of where it was found
# rjust(): #Returns a right justified version of the string
# rpartition(): #Returns a tuple where the string is parted into three parts
# rsplit(): #Splits the string at the specified separator, and returns a list
# rstrip(): #Returns a right trim version of the string
# split(): #Splits the string at the specified separator, and returns a list
# splitlines(): #Splits the string at line breaks and returns a list
# startswith(): #Returns true if the string starts with the specified value
# strip(): #Returns a trimmed version of the string
# swapcase(): #Swaps cases, lower case becomes upper case and vice versa
# title(): #Converts the first character of each word to upper case
# translate(): #Returns a translated string
# upper(): #Converts a string into upper case
# zfill(): #Fills the string with a specified number of 0 values at the beginning

# Exercício 5: Acesse os três primeiros caracteres de uma string.

lista = ["oi", "olá", "tudo bem?", "bom dia"]
lista.pop(3)
print(lista)

# Exercício 6: Acesse todos os elementos de uma lista, exceto o primeiro e o último.

lista1 = ["oi", "olá", "tudo bem?", "bom dia"]
lista1.pop(0 and 3)
print(lista1)

# < Desafio: Calculadora de Média >
# Instruções: Peça ao usuário que insira três notas (por exemplo, de 0 a 10). Use a função input() para obter as notas como entrada do usuário e converta-as 
# em números de ponto flutuante. Calcule a média das três notas.
# Com base na média, forneça uma avaliação:
# Se a média for maior ou igual a 7, imprima "Aprovado".
# Se a média for maior ou igual a 5 e menor do que 7, imprima "Recuperação".
# Se a média for menor do que 5, imprima "Reprovado".
# Certifique-se de lidar com possíveis erros, como entradas inválidas (por exemplo, notas fora do intervalo de 0 a 10).
# A SAÍDA PRECISA FICAR ASSIM NÃO COM OS MESMOS NÚMEROS, MAS
# PRECISA SER ASSIM:
# Por favor, insira a primeira nota: 8.5
# Por favor, insira a segunda nota: 6.0
# Por favor, insira a terceira nota: 4.5
# Sua média é 6.33 e você está em Recuperação.

nota1 = input(float("digite a primeira nota de 0 a 10:\n"))
nota2 = input(float("digite a segunda nota de 0 a 10:\n"))
nota3 = input(float("digite a terceira nota de 0 a 10:\n"))
media = (nota1 + nota2 + nota3)/3 
if media >= 7: 
    print("Aprovado")
elif media >= 5 :
    print("Recuperação")
else:
    print("Reprovado")
