import matplotlib.pyplot as plt

#La mayotia de los graficos debijan sus elemnetos
#a partir de X, Y
x=["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]
#valor del mercado
y=[30, 400, 500, 20]
#para crear el grafico debemos darle los datos a la
#libreria mediante plt.bar
plt.bar(x, y)
plt.title("Grafico de barras")
plt.xlabel("Equipos")
plt.ylabel("Valor en M$")
plt.savefig('images/barras.png')
plt.show()
#podemos guardar los graficos en imagenes
