print("_"*25,"\n","-> Loops:","\n","While:")

#While:
#É uma estrutura que permite repetir a execução de um bloco de código enquanto uma condição for verdadeira:

o = 1
while o < 10:
    print(o)
    o += 7
print("terminou")

#Nesse caso o < 10 é a condição, e no momento que ela se torna verdadeira a estrutura "while" deixa de executar o bloco de código

#Obs.: += vai adicionar a uma variável um número, ou até mesmo o valor de outra variável

print("_"*25,"\n","For:")

#For:
#É uma estrutura de repetição que permite executar um bloco de código para cada item de uma sequência, ela é executada da seguinte forma:
#Palavra-chave for -> uma variável que representa o item atual da sequência -> a palavra-chave in -> a sequência sobre a qual iterar -> dois pontos (:)

i = "lídia", "louise", "mc"
for x in i:
    print(x)

#No exemplo a estrutura "for" executa o bloco de código uma vez para cada item da sequência

print("_"*25, "\n", "For: + range")
#Range:
#É uma ferramenta que gera sequências de números inteiros e é usada principalmente para controlar loops:

for y in range(5):
    print(y)

#Nessa ferramenta podemos colocar 3 números:
#O primeiro será de onde a sequência vai começar
#O segundo será até onde a sequência irá (lembrando que não inclui o número digitado)
#O terceiro será de quantos em quantos números a sequência pulará

for z in range(4,20,3):
    print(z)
