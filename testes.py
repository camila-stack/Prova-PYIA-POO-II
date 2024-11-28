class Veiculo:
    def movimentar(self):
        return 'Veículo está em movimento.'

class Carro(Veiculo):
    def movimentar(self):
        return 'O Carro está sendo dirigido'

class Moto(Veiculo):
    def movimentar(self):
        return 'A Moto está acelerando'
    

carro1 = Carro()
moto1 = Moto()

print(carro1.movimentar())
print(moto1.movimentar())