idade = int(input("Insira sua idade: "))
categoria = input("Insira sua categoria (estudante, aposentado, deficiente.): ")
dia = input("Insira o dia da semana: ")

desconto = 0

if idade >= 60:
    desconto = 0.40
elif categoria == "estudante" and (dia == "segunda" or dia == "terça"):
    desconto = 0.10
elif categoria == "aposentado":
    desconto = 0.20
elif categoria == "deficiente" and dia == "quarta":
    desconto = 0.25

if desconto > 0:
    print("Você tem direito a {:.0%} de desconto.".format(desconto))
else:
    print("Você não tem direito a nenhum desconto.")
