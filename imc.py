""" IMC """
""" ingreso de variables """
peso = float(input("Ingresar el peso en [Kg]: \n"))
alturaCm = float(input("Ingresar la altura en [Cm]: \n"))

""" Calculos IMC """

altura = alturaCm/100 # conversion Cm a Mt
imc = peso / altura**2

""" IMC Clasificación OMS """

imcClass = ""

if imc >= 40:
    imcClass = "Obesidad Grado III"
elif imc < 40 and imc >= 35:
    imcClass = "Obesidad Grado II"
elif imc < 35 and imc >= 30:
    imcClass = "Obesidad Grado I"
elif imc < 30 and imc >= 25:
    imcClass = "Sobrepeso"
elif imc < 25 and imc >= 18.5:
    imcClass = "Adecuado"
else:
    imcClass = "Bajo Peso"

""" Resultado en pantalla """

print(f"Su IMC es {imc:.2f}")
print(f"La clasificación OMS es {imcClass}")