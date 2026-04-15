# ex25.py
print("Cardapio:")
print("1 - Hamburguer R$ 15.00")
print("2 - Pizza R$ 30.00")
print("3 - Refrigerante R$ 8.00")

opcao = int(input("Escolha uma opcao: "))

if opcao == 1:
    print("Voce escolheu Hamburguer")
elif opcao == 2:
    print("Voce escolheu Pizza")
elif opcao == 3:
    print("Voce escolheu Refrigerante")
else:
    print("Opcao invalida")