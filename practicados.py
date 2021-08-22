import random  #lib sirve para generar datos aleatoriamente
import matplotlib.pyplot as plt #lib sirve para crear graficas
#generar numero aleatorio          print(random.randint(1, 20))
#generar numero aleatorio con numeros pares         print(random.randrange(10, 100, 2))

#reacomodar lista
lista = [1,2,3,4,5,6,7,8,9,10]
print("lista original", lista)
#mixear lista o mezclar al azar
random.shuffle(lista)
print("lista mixeada", lista)
#genera una grafica de campana de GAUSS
campana = [random.gauss(1,0.5) for i in range(1000)]
#arma la grafica
plt.hist(campana, bins=15)
#muestra la grafica
plt.show()
