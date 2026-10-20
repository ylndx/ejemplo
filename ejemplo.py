#Importamos la libreria
import csv

#Abre datos.csv, que está dentro de la carpeta datos.
with open("datos\\datos.csv", newline="", encoding="utf-8") as archivo:
    #Lee y muestra cada fila del archivo.
    for fila in csv.reader(archivo):
        print(fila)



