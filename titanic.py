import pandas as pd

df = pd.read_csv('titanic.csv')

print("1.¿Cuántos pasajeros existen en el conjunto de datos y cuántos identificadores distintos hay?")

cont = 0
for i in range(len(df)):
    cont += 1

print("Número de pasajeros: ", cont)
print(len(df['PassengerId'].unique()))
print(len(df))




