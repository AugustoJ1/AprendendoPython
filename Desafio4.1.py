import random

def main():
    n_plateia = int(input("Insira um número de 1 a 5: "))
    n_magico = random.randint(1,5)
    if n_plateia < n_magico:
        print("Fala um numero maior.")
    elif n_plateia == n_magico:
        print("Acertou em cheio")
    else:
        print("Chute mais baixo!!")
    5
    print(n_magico)

main()