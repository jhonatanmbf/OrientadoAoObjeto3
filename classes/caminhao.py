from classes.automovel import Automovel

class Caminhao(Automovel):
  def __init__(self, anoFabricacao, velocidade):
    super().__init__(anoFabricacao,velocidade)
  def acelerar(self):
    return self.velocidade + 16;
  def frear(self):
    return self.velocidade - 7;