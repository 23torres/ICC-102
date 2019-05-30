def CalcularPotencia(b, e):
    acumulado = 1

    while e>0:
        acumulado = acumulado * b
        e = e - 1

    return acumulado

base = -1
exponente = -1
while base <= 0 or exponente <= 0:
    base = int(input("Digite la base: "))
    exponente = int(input("Digite el exponente: "))

    if base <= 0 or exponente <= 0:
        print("Sólo psitivos.")

potencia = CalcularPotencia(base, exponente)
print(potencia)
