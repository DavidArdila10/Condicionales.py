#1. Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo.


numero=float(input("Digite un numero    "))


if numero>0:
    print("El numero es positivo")
elif numero==0:
    print("El numero ingresado es cero")
else:
    print("El numero es negativo")


#2. Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor.
a=float(input("Digite el primer numero  "))
b=float(input("Digite el segundo numero  "))
if a>b:
    print("El primer numero es mayor y el segundo es menor")
elif b>a:
    print("El segundo numero es mayor y el primero menor")


#3. Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos
a=int(input("Digite el primer numero  "))
b=int(input("Digite el segundo numero  "))
c=int(input("Digite el tercer numero  "))

menor = a
mayor = a

if b < menor:
    menor = b

elif b > mayor:
    mayor = b

if c < menor:
    menor = c

elif c > mayor:
    mayor = c

print("El menor número es:", menor)
print("El mayor número es:", mayor)

#4. Dados dos números A y B, sumarlos si A es menor que B o sino restarlos
a = float(input("Digite el primer numero: "))
b = float(input("Digite el segundo numero: "))

if a < b:
    resultado = a + b
else:
    resultado = a - b

print("El resultado es:", resultado)

#5. Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible
a = float(input("Escriba el primer número: "))
b = float(input("Escriba el segundo número: "))

if b == 0:
    print(f"La división no es posible, por cuanto la división por cero no está definida.")
else:
    division = a / b
    print(f"El cociente entre los dos números es {division}")

#6. Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos
a = float(input("Digite el primer numero: "))
b = float(input("Digite el segundo numero: "))

if a <0 or b < 0:
    resultado= a+b
else:
    resultado= a*b

print("El resultado es:", resultado)

#7. Escribir un algoritmo que determine si un año es bisiesto o no.
año = int(input("Digite un año: "))


if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0): #Si el año es divisible en 4 y no es divisible en 100 OR el año es divisible en 400
    print(año, "es un año bisiesto.")
else:
    print(año, "no es un año bisiesto.")
