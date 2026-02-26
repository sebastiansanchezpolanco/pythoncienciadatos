import matplotlib.pyplot as plt

#La mayotia de los graficos debijan sus elemnetos
#a partir de X, Y
x=["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]
#valor del mercado
y=[30, 400, 500, 20]
#para crear el grafico debemos darle los datos a la
#libreria mediante plt.bar
plt.scatter(x, y)
plt.title("Grafico de dispersion")
plt.xlabel("Equipos")
plt.ylabel("Valor en M$")
plt.savefig('images/dispersion.png')
plt.show()
#podemos guardar los graficos en imagenes
