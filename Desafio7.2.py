#Construir uma função que recebe 2 notas e outras que calcula a média
import statistics

def receber_notas():
    n1 = float(input("Insira a primeira nota: "))
    n2 = float(input("Insira a segunda nota: "))
    return n1, n2

def average(receber_notas):
    soma = float(receber_notas[0] + receber_notas[1])
    media = soma / 2
    return print(media)

average(receber_notas())
