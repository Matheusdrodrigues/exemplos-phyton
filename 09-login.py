nome_de_usuario = str(input("digite nome de usuario: "))
senha = int(input("digite a senha: "))

if senha == 123 and nome_de_usuario == "admin":
    print ("acesso librado")
else: 
    print ("acesso negado")