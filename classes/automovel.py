class Automovel():
  def __init__(self, anoFabricacao, velocidade):
    self.anoFabricacao = anoFabricacao;
    self.velocidade = velocidade;
  def acelerar(self):
    return self.velocidade + 10;
  def frear(self):
    return self.velocidade - 5;