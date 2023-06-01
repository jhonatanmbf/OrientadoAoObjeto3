from classes.carro import Carro
from classes.caminhao import Caminhao
from classes.caminhonete import Caminhonete
from classes.moto import Moto

def main():
  carro = Carro('2022', 0);
  print(f"Os atributos do carro: Ano:{carro.anoFabricacao}, Velocidade:{carro.velocidade}")
  carro.velocidade = carro.acelerar()
  print(f"O carro acelerou sua velocidade agora é {carro.velocidade}")
  carro.velocidade = carro.acelerar()
  print(f"O carro acelerou de novo sua velocidade agora é {carro.velocidade}")
  carro.velocidade = carro.frear()
  print(f"O carro freou sua velocidade agora é {carro.velocidade}")
  
  print("\n")

  caminhao = Caminhao('2022', 0);
  print(f"Os atributos do caminhao: Ano:{caminhao.anoFabricacao}, Velocidade:{caminhao.velocidade}")
  caminhao.velocidade = caminhao.acelerar()
  print(f"O caminhao acelerou sua velocidade agora é {caminhao.velocidade}")
  caminhao.velocidade = caminhao.acelerar()
  print(f"O caminhao acelerou de novo sua velocidade agora é {caminhao.velocidade}")
  caminhao.velocidade = caminhao.frear()
  print(f"O caminhao freou sua velocidade agora é {caminhao.velocidade}")
  
  print("\n")

  caminhonete = Caminhonete('2022', 0);
  print(f"Os atributos do caminhonete: Ano:{caminhonete.anoFabricacao}, Velocidade:{caminhonete.velocidade}")
  caminhonete.velocidade = caminhonete.acelerar()
  print(f"O caminhonete acelerou sua velocidade agora é {caminhonete.velocidade}")
  caminhonete.velocidade = caminhonete.acelerar()
  print(f"O caminhonete acelerou de novo sua velocidade agora é {caminhonete.velocidade}")
  caminhonete.velocidade = caminhonete.frear()
  print(f"O caminhonete freou sua velocidade agora é {caminhonete.velocidade}")
  
  print("\n")

  moto = Moto('2022', 0);
  print(f"Os atributos do moto: Ano:{moto.anoFabricacao}, Velocidade:{moto.velocidade}")
  moto.velocidade = moto.acelerar()
  print(f"O moto acelerou sua velocidade agora é {moto.velocidade}")
  moto.velocidade = moto.acelerar()
  print(f"O moto acelerou de novo sua velocidade agora é {moto.velocidade}")
  moto.velocidade = moto.frear()
  print(f"O moto freou sua velocidade agora é {moto.velocidade}")


if __name__ == "__main__":
  main();