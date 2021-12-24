def main():
    notas = []
    for i in range(0, 5):
        nota = int(input("Insira a sua nota: "))
        notas.append(nota)
    for nota in notas:
        print(nota)

main()