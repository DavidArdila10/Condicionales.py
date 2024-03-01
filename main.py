#Primera pregunta: 

print("Primera pregunta: Calcular el área de un triángulo")

base = float(input("Digite el número de la base: "))
altura = float(input("Digite el número de la altura: "))
operacion = base * altura
resultado = print(f"El área del triángulo es {operacion}")

#Segunda pregunta: 
print("Segunda pregunta: Ingresar dos números por teclado y sumarlos")

numero_1 = float(input("Digite el primer número: "))
numero_2 = float(input("Digite el segundo número: "))
operacion_suma = numero_1 + numero_2
resultado_suma = print(f"La suma de los dos números es {operacion_suma}")

#Tercera pregunta: 
print("Tercera pregunta: Ingresar un número y visualzar el número elevado al cuadrado")

numero_a_elevar_al_cuadrado = float(input("Digite el número que quiere que sea elevado al cuadrado: "))
operacion_potencia = numero_a_elevar_al_cuadrado**2
resultado_potencia = print(f"El número elevado al cuadrado es {operacion_potencia}")

#Cuarta pregunta: 
print("Cuarta pregunta: Escribir un algoritmo que convierta de euros a dolares")

precio_euro = float(input("Ingresa el costo del euro en dolares: "))
euros = float(input("Ingresa la cantidad de euros: "))
dolares = euros * precio_euro
resultado_conversion = print(f"Tus euros a dolares equivalen a: {dolares}")

#Quinta pregunta: 
print("Quinta pregunta: Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perimetro")

numero_lado_cuadrado = float(input("Digite el número que corresponde al lado del cuadrado: "))
area_cuadrado = numero_lado_cuadrado*numero_lado_cuadrado
perimetro_cuadrado = numero_lado_cuadrado+numero_lado_cuadrado+numero_lado_cuadrado+numero_lado_cuadrado
resultado_potencia = print(f"El área del cuadrado es {area_cuadrado} cms y su perimetro es {perimetro_cuadrado} cms")

#Sexta pregunta: 
print("Sexta pregunta: Escribir un algoritmo que determine el área y el volumen de un cilindro")

radio = float(input("Digite el número del radio del cilindro (en milimetros): "))
altura = float(input("Digite el número de la altura del cilindro (en centimetros): "))
radio_cms = radio / 10
numero_pi = 3.1416 
area_cilindro = 2 * numero_pi * radio_cms * altura +  2 * numero_pi * radio_cms**2
volumen_cilindro =  numero_pi * (radio_cms**2) * altura
resultado_cilindro = print(f"El área del cilindro es {area_cilindro} cms2 y su volumen es {perimetro_cuadrado} cms3")

#Septima pregunta: 
print("Septima pregunta: Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área  del círculo inscrito")

radio_circunferencia = float(input("Digite el número del radio de la circunferencia: "))
longitud_circunferencia = 2 * numero_pi * radio_circunferencia
area_circuferencia =  numero_pi * (radio_circunferencia**2)
resultado_circuferencia = print(f"La longitud de la circunferencia es {longitud_circunferencia} y su área es {area_circuferencia}")

#Octava pregunta: 
print("Octava pregunta: Calcular el promedio de tres (3) números ingresados por teclado")

numero_uno = float(input("Digite el primer número: "))
numero_dos = float(input("Digite el segundo número: "))
numero_tres = float(input("Digite el tercer número: "))
promedio = (numero_uno + numero_dos + numero_tres)/3
resultado_promedio = print(f"El promedio de los tres números es {promedio}")












