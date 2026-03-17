quantidade_adquirida = int(input("digite a quantidade"))
preço_unitário = float(input("digite o preço unitario"))
produto = str(input("digite o nome do produto"))                          
total = quantidade_adquirida * preço_unitário

if quantidade_adquirida <=5:
    desconto = 2
if quantidade_adquirida >5 <=10:
    desconto = 3
if quantidade_adquirida >10:
    desconto = 5

total_a_pagar = total - (total / 100 * desconto)
print ("o valor total do produto" ,produto ,("é") ,total)
print ("o valor total com desconto é" ,total_a_pagar)