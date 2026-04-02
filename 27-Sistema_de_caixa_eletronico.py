import os
os.system ("cls")

nome = str(input("nome do usuario: "))
dinheiro = 1000

while True:
  print("1-ver saldo")
  print("2-sacar")
  print("3-depositar")
  print("4-sair")
  ação = int(input(f"{nome} escolha as opções a baixo:"))

  if ação == 1:
    print(nome, "seu saldo é igual a: ", dinheiro)


  elif ação == 2:
    valor_a_sacar = float(input("insira o valor que deseja sacar:"))
    
    if valor_a_sacar > dinheiro:
      print("saldo insufisciente!!")
    elif valor_a_sacar == 0:
      print("valor invalido")
    else:
      dinheiro -= valor_a_sacar
  elif ação == 3:
    valor_a_depositar = float(input("quanto deseja depositar:"))
    dinheiro += valor_a_depositar
  else: break
print("obrigado", nome, "tenha um bom dia")