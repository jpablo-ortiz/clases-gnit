# 1. Vamos a pedir unos datos al cliente para ser usados

nombre = input("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))
tiene_pase_de_conduccion_texto = input("Tienes pase de conducción (si, no): ") 

#! PROCESAR LOS DATOS - CONDICIONALES e imprimir

# Convertir la respuesta del usuario en un booleano (True, False)
if tiene_pase_de_conduccion_texto == "si":
    tiene_pase_de_conducir = True
else:
    tiene_pase_de_conducir = False

# La persona podrá conducir sola si es mayor de edad y tiene pase de conducción
if edad >= 18 and tiene_pase_de_conducir:
    print(f"Señor(a) {nombre} usted puede conducir solo")
# La persona podrá conducir con un adulto, si tiene pase de conducir y es menor de edad
elif edad < 18 and tiene_pase_de_conducir:
    print(f"Señor(a) {nombre} usted puede conducir con un adulto a cargo")
## La persona no podrá conducir si no tiene pase de conducir.
else:
    print(f"Señor(a) {nombre} lastimosamente usted no puede conducir")