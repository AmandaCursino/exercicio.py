idade = int(input("Insira a idade da pessoa: "))
alfabetizado = input("A pessoa é alfabetizada?: ")

if idade > 25 and alfabetizado == "sim":
    print("A pessoa é alfabetizada e tem mais de 25 anos.")
else:
    print("A pessoa não atende aos critérios de alfabetização e idade.")
