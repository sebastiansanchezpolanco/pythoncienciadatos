import pandas as pd

#Vamos a leer datos de nuestro CSV
#Creamos un dataframe a partir del fichero
df=pd.read_csv('data/datos.csv', delimiter=';')
#imprimimos el DataFRame
print("--------DataFrame completo--------")
print(df)
#podemos indicar el numero de filas a mostrar
print("--------Primeras 5 filas--------")
print(df.head())
print("--------Primeras 7 filas--------")
print(df.head(8))
diccionario=df.to_dict(orient='records')
for registro in diccionario:
    print(registro)
df_media=df['edad'].mean()
print(df_media)
df_group=df.groupby('ocupacion')
print(df_group.size())
