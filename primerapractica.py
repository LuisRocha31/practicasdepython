nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
edad = int(edad)
if edad >=18 and edad <100:
      print(f"Hola {nombre} tienes {edad} años, ya eres mayor de edad")
elif edad >=200:
      print(f"Hola {nombre} tienes {edad} años, eres inmortal!!!")
else:
       print(f"Hola {nombre} tienes {edad} años, aun eres menor de edad")

for i in range(0, 10):
    print(i)
    