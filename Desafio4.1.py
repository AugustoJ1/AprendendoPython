import random

def main():
    n_magico = random.randint(1,5)
    n_plateia = 0
    while n_plateia != n_magico:
        n_plateia = int(input("Insira um número de 1 a 5: "))
        if n_plateia < n_magico:
            print("Fale um numero maior.")
        elif n_plateia == n_magico:
            print("Acertou em cheio")
            break
        else:
            print("Chute mais baixo!!")
        print(n_magico)

main()