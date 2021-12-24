#Construir uma função que recebe 2 notas e outra que calcula a média

def receber_notas():
    n1 = int(input("Insira a primeira nota: "))
    n2 = int(input("Insira a segunda nota: "))
    return average(n1, n2)

def average(n1, n2):
    media = (n1 + n2) / 2
    return media

def aprovados(media):
    if media >= 7.0:
        print(f'Parabéns você foi aprovado com a média {media:.1f}')
    else:
        print(f'Infelizmente você foi reprovado com a média {media:.1f}')


aprovados(receber_notas())
