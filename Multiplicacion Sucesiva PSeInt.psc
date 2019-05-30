Algoritmo CalcularMultiplicaciónSucesiva
	Escribir "Digite un valor: "
	Leer valor
	Escribir "Digite otro valor: "
	Leer valor2
	resultado <- 0
	Mientras valor2 != 0 Hacer
		resultado <- resultado + valor
		valor2 <- valor2 - 1
		Escribir resultado
	FinMientras
FinAlgoritmo

