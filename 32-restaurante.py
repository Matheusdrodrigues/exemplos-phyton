import os
os.system("cls")

def dividir(conta, numero_de_pessoas):
    resultado = conta / numero_de_pessoas
    return resultado

print("Olá seja bem vindo ao App Minha Conta!")

conta = float(input("Por favor insira o valor de sua conta:"))
numero_de_pessoas = int(input("Por favor insira o numero de clientes:"))

resultado = conta / numero_de_pessoas

print(f"Total da conta: {conta}")
print(f"Numero de clienes: {numero_de_pessoas}")
print(f"Valor individual a ser pago: {resultado}")
