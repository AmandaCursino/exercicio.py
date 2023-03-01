v = float(input("Insira o primeiro número: "))
x = float(input("Insira o segundo número: "))
y = float(input("Insira o terceiro número: "))

if v > x + y or x > v + y or y > v + x:
    print("Um dos números é maior que os outros dois.")
else:
    print("Não existe um número maior que a soma dos outros dois.")
    
