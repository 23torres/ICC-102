Algoritmo ModuloIterativo
	Escribir "Digite el divisor: "
	Leer divisor
	Escribir "Digite el dividende: "
	Leer dividendo
	Si dividendo > 0 y divisor > 0 Entonces
		resultado = CalcularResiduo(divisor, dividendo)
	SiNo
		Escribir "S�lo positivos"
	FinSi
	Escribir resultado
FinAlgoritmo

Funcion divisor <- CalcularResiduo(divisor, dividendo)
	Repetir
	Hasta Que divisor > dividendo
	divisor = divisor - dividendo
FinFuncion

