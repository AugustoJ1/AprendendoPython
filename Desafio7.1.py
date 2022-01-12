# Construir uma função que recebe duas notas e calcula a média
import statistics
def average(n1, n2):
    soma = n1 + n2
    media = soma / 2
    return print(media)

n1 = int(input("Insira a primeira nota: "))
n2 = int(input("Insira a segunda nota: "))
average(n1, n2)

print(statistics.mean([n1, n2])) 
