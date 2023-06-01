from classes.automovel import Automovel

class Caminhonete(Automovel):
  def __init__(self, anoFabricacao, velocidade):
    super().__init__(anoFabricacao,velocidade)
  def acelerar(self):
    return self.velocidade + 17;
  def frear(self):
    return self.velocidade - 8;