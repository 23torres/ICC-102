#temperaturas = [float(x) for x in input().split()]

temperaturas = []
temperaturaActual = float(input("Digite una nueva temperatura: "))
#suma = temperaturaActual
while temperaturaActual > 0:
    temperaturas.append(temperaturaActual)
    temperaturaActual = float(input("Digite una nueva temperatura: "))
    #suma += temperaturaActual

#print("Promedio: {0}".format(suma / len(temperaturas)))
print("Promedio: {0}".format(sum(temperaturas) / len(temperaturas)))
