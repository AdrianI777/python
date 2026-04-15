# ex19.py
idade = int(input("Idade: "))
gestante = input("Gestante (sim/nao): ")

if idade >= 60 or gestante == "sim":
    print("Senha preferencial")
else:
    print("Atendimento normal")