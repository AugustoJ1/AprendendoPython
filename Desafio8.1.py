class Carro(object):
    def __init__(self, estado, nome):
        self.estado = estado
        self.nome = nome

    def mostrar_infos(self):
        print(f"O carro {self.nome} tem o estado {self.estado}")

bmw = Carro('semi-novo', 'BMW')
mercedes = Carro('novo', 'Meca')
ferrari = Carro('novo', 'Ferrari')

bmw.mostrar_infos()
mercedes.mostrar_infos()
ferrari.mostrar_infos()
