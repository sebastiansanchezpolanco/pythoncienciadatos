import matplotlib.pyplot as plt

#La mayotia de los graficos debijan sus elemnetos
#a partir de X, Y
equipos=["Atletico de Madrid", "Real Madrid", "Barcelona", "Betis"]
#valor del mercado
valores=[30, 400, 500, 20]
#para crear el grafico debemos darle los datos a la
#libreria mediante plt.bar
plt.pie(valores, labels=equipos)
plt.title("Grafico de quesitos")
plt.savefig('images/quesitos.png')
plt.show()
#podemos guardar los graficos en imagenes
