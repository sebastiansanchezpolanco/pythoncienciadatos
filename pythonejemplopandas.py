import pandas as pd
#las series tienen que ser iguales entre ellas
#todas las series deben tener la misma "longitud de datos"
#vamos a crear un diccionario
datos={
    "Nombres": ["Ana", "Adrian", "Lucia", "Antonia"],
    "Edad": [23, 34, 32, 20],
    "Ciudades":["Madrid", "Barcelona", "Salamanca", "Valencia"]
}
#Estas series de datos se almacenan dentro de objetso
#llamadas DataFrame de las librerias pandas
df=pd.DataFrame(datos)
#Mis primeros datos
print("--------DataFrame total-------")
print(df)
print("--------DataFrame filtrado-------")
dffiltrado=df[df["Edad"]>23]
print(dffiltrado)
print("--------DataFrame ordenado-------")
dfordenado=df.sort_values("Nombres")
print(dfordenado)