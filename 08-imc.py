peso = float(input("digite o peso"))
altura = float(input("digite a altura"))

imc = peso / (altura * altura)
print ("seu imc é igual a" ,imc)

if imc < 16.9:
    print ("muito abaixo do peso")
if imc >= 17 <= 18.4:
    print ("abaixo do peso")
if imc >= 18.5 <= 24.9:
    print ("peso normal")
if imc >= 25 <= 29.9:
    print ("acima do peso")
if imc >= 30 <= 34.9:
    print ("obesidade grau I")
if imc >= 35 <= 40:
    print ("obesidade grau II")
if imc > 40:
    print ("obesidade grau III")