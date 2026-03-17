nome_do_professor = str(input("nome do professor"))
nivel = int(input("nivel do professor"))
quantidade_de_aula = int(input("quantidade de aulas do professor"))

if nivel == 1: 
        valor = 12
if nivel == 2:
        valor = 17
if nivel == 3:
        valor = 25
 
salario = quantidade_de_aula * valor
print ("o salario do professor" ,nome_do_professor ,("é de") ,salario)