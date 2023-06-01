from classes.automovel import Automovel

class Moto(Automovel):
  def __init__(self, anoFabricacao, velocidade):
    super().__init__(anoFabricacao,velocidade)
  def acelerar(self):
    return self.velocidade + 18;
  def frear(self):
    return self.velocidade - 9;