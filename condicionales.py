#Declaramos una variable
calificacion = input("Introduce tu calificacion de la AZ900")
calificacion = int(calificacion)
#preguntamos si la calificacion es  menor a 700
if calificacion < 700:
    print("Veees , por no estudiar")#Si es menor a 700 muestra esto
elif calificacion ==700:
    print("Panzazooo")
elif calificacion >= 1000:
    print("mientes!! no puedes sacar mas de mil")
else:# si no se cumple el if anterior, pasa a esta lìnea
    print("Felcidades pasa, por tu certificado")#Se ejecuta si alguno de los if se cumple

#Verificador de mayupria de edad
edad =input("introduce tu edad")
edad = int(edad)

if edad >= 18 and edad <= 100:
    print("bienvenido al mamitas")
elif edad > 100:
    print("Si vienes acompañdo de tus abuelitos, si te podemos fiar.")
elif edad < 0:
    print("Ni que fueras viejro del tiempo")
else :
    print("no puedes llevarte los cigarros")
#En python no hay Swtch case: