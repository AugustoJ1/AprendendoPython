# Classe calculadora que contém os seguintes métodos:
# - Somar
# - Subtrair
# - Multiplicar 
# - Dividir
# PS: Esses métodos funcionam apenas com 2 números
# PS2: Todos os métodos retornam um valor
#   A classe também contém as propriedades (atributos):
#   - primeiro_valor
#   - segundo_valor 
# PS3: Os valores são passados em parâmetro
# PS4:Os valores vão ser lidos do usuário(input)


class calculadora(object):
    def somar(self,primeiro_valor,segundo_valor):
        s = primeiro_valor + segundo_valor
        return s
    
    def multiplicar(self, primeiro_valor, segundo_valor):
        m = primeiro_valor * segundo_valor
        return m
    
    def subtrair(self, primeiro_valor, segundo_valor):
        sub = primeiro_valor - segundo_valor
        return sub

    def dividir(self, primeiro_valor, segundo_valor):
        d = primeiro_valor/segundo_valor
        return d

p1 = input("Insira o primeiro valor: ")
p1 = int(p1)
p2 = input("Insira o segundo valor: ")
p2 = int(p2)

resultado = calculadora()
print(resultado.somar(p1, p2))
print(resultado.dividir(p1,p2))
print(resultado.subtrair(p1,p2))
print(resultado.multiplicar(p1,p2))
