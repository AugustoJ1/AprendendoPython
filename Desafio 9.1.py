# Classe Carro:
    # Modelo => Definidos pelo construtor(Quem define é a loja (classe)) => Tem um valor inicial para cada um
    # Ano => Definidos pelo construtor(Quem define é a loja (classe)) => Tem um valor inicial para cada um
    # Estado => Definidos pelo construtor(Quem define é a loja (classe)) =>Tem um valor inicial para cada um
    # Comprado => Vai ser falso para todos => Valor inicial Padrão => É uma variável de classe(e não de instância)

    # liga_desliga() => Liga e desliga o carro => Obrigatório para dirigir/fazer test drive
    # acelerar() => Só pode acelerar depois de comprar o carro... Mas vai tentar mesmo assim
    # test_drive() => Só pode fazer antes de comprar => Não posso acelerar
    # comprar() => Só pode comprar uma vez
    # dirigir() => Você pode somente depois de comprar o carro => pode acelerar

    # Modelo, Ano e Estado => são atributos de instância (Construtor)
    # Comprado => Atributo de classe (Valor padrão inicial)
    # Ligar e Desligar, Acelerar, Fazer Test Drive, dirigir e Comprar => São Métodos

class Carro(object):
    comprado = False

    def __init__(self, modelo, ano, estado):
        self.modelo = modelo
        self.ano = ano
        self.estado = estado
    
    def liga_desliga(self, status):
        if status: # booleano
            print("Você ligou o carro")
        else:
            print("Você desligou o carro")

    def acelerar(self):
        return self.comprado
       
    def test_drive(self):
        if(not self.comprado):
            print("Você vai fazer o test drive")
            self.liga_desliga(True)
            print("Você está fazendo test drive")
            if(self.acelerar()):
                print("Você está acelerando")
            else:
                print("Você não pode acelerar")
            self.liga_desliga(False)
            print("Você terminou de fazer o test drive")
        else:
            print("Você não pode fazer o test drive")

    def comprar(self):
        if(self.comprado):
            print(f"Você já comprou o carro")
            return # Interrompe o ciclo / estilo um break
        self.comprado = True
        print("Você comprou o carro!")

    def dirigir(self):
        if(self.comprado):
            print("Você vai dirigir")
            self.liga_desliga(True)
            print("Você está dirigindo")
            if(self.acelerar()):
                print("Você está acelerando")
            else:
                print("Você não pode acelerar")
            self.liga_desliga(False)
            print("Você terminou de dirigir")
        else:
            print("Você só pode dirigir se comprar o carro")


ferrari = Carro('Ferrari', '2019', 'Novo')
bmw = Carro(ano='2017', estado='Semi-novo', modelo='2017')

ferrari.dirigir()
print(".")
ferrari.test_drive()
print(".")
ferrari.comprar()
print(".")
ferrari.comprar()
print(".")
ferrari.dirigir()
print(".")
bmw.test_drive()
print(".")
bmw.dirigir()
print(".")
bmw.comprar()
print(".")
bmw.dirigir()