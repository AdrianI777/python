# ex17.py
usuario = input("Usuario: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "123":
    print("Login realizado")
else:
    print("Usuario ou senha incorretos")