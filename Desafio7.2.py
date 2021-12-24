#Construir uma função que recebe 2 notas e outras que calcula a média
import statistics

def receber_notas():
    n1 = int(input("Insira a primeira nota: "))
    n2 = int(input("Insira a segunda nota: "))
    return n1, n2
'''
def average(receber_notas):
    soma = receber_notas
    media = soma / 2
    return print(media)
'''
receber_notas()
# average(receber_notas)

print(statistics.mean(receber_notas))
