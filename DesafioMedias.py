# Classe Aluno que contém os seguintes atributo:
# - Nome => string
# - Status => Aprovado ou Reprovado (booleano)
# - Nota1 => float
# - Nota2 => float
# métodos:
# - Mostrar informações (mostrar_informacoes) => Fala o nome do aluno e se ele foi aprovado ou não 
# - Calcular Média (calcular_media) => calcula e retorna a média do aluno
# - Inserir nota (inserir_nota) =>Adiciona valor nas notas do aluno (2 parâmetros de nota)
#   Regras:
#   - Para passar ele precisa de 6
#   - Nome será enviado no construtor
#   - Nota1 e Nota2 será enviado por parâmetro => Inserir Nota

class aluno(object):
    status = False

    def __init__(self, nome):
        self.nome = nome 

    def inserir_nota(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def calc_media(self):
        return ((self.nota1 + self.nota2)/2)

    def mostrar_informacoes(self):
        status = self.calc_media() >= 6
        if status:
            print(f"O {self.nome} foi aprovado")
        else:
            print(f"O {self.nome} foi reprovado")

felipe = aluno("Felipe")
felipe.inserir_nota(9, 8)
felipe.mostrar_informacoes()
