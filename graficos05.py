import matplotlib.pyplot as plt

productos=[]
ventas=[]
#Deseamos peridr 5 productos
for i in range(1,6):
    produc=input("Nombre del producto: ")
    productos.append(produc)
    vent=int(input("Introduzca el numero de venta: "))
    ventas.append(vent)
plt.pie(ventas, labels=productos)
plt.show()
    