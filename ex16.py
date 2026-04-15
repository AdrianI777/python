# ex16.py
idade = int(input("Idade: "))
carteira = input("Tem carteira (sim/nao): ")

if idade >= 18 and carteira == "sim":
    print("Pode dirigir")
else:
    print("Nao pode dirigir")