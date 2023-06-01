from classes.automovel import Automovel

class Carro(Automovel):
  def __init__(self, anoFabricacao, velocidade):
    super().__init__(anoFabricacao,velocidade)
  def acelerar(self):
    return self.velocidade + 15;
  def frear(self):
    return self.velocidade - 6;