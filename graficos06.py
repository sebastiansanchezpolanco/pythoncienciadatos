import matplotlib.pyplot as plt

semana=("Lunes", "Martes", "Miercoles", "Jueves", "Viernes",)
temperaturas=[]
for dia in semana:
    print(f"Temperatura del dia {dia}")
    temp=int(input())
    temperaturas.append(temp)
plt.plot(semana, temperaturas, label="Semana 1")
temperaturas2=[20,17,13,8,6]
plt.plot(semana, temperaturas2, label="Semana 2")
plt.legend()
plt.title("Temperaturas de febrero")
plt.xlabel("Dia de la semana")
plt.ylabel("Temperatura")
plt.show()