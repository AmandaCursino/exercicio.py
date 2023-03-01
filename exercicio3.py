idade = int(input("Insira a idade: "))
autorizacao = input("Tem autorização dos pais?: ")

if idade >= 18 or autorizacao == "sim":
    print("Você pode participar.")
else:
    print("Você não pode participar.")
