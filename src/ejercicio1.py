import csv
from collections import namedtuple
from datetime import datetime

VariacionTemperatura = namedtuple('VariacionTemperatura', 'fecha, variacion')

def lee_variaciones_temperatura(ruta):
    #para leer un fichero de texto en python
    #encoding = 'utf-8' esta es la tabla de caracteres, se guardan en el sistema los numeros que corresponden a un caracter según la tabla
    with open(ruta, encoding = 'utf-8') as f: 
        lector = csv.reader(f)
        next(lector) #next "consume" un dato de la secuencia
        #objetivo, lista cuyos elementos son tuplas con dos elementos cada una
        res = []
        #Trabajar con f
        for fecha, variacion in lector: 
            fecha = datetime.strptime(fecha,"%d/%m/%Y").date() #tengo que convertir la fecha a date
            variacion = float(variacion)
            
            tupla = VariacionTemperatura(fecha, variacion)
            res.append(tupla)
        return res
            

if __name__=="__main__":
    datos = lee_variaciones_temperatura("data/monthly_csv.csv")
    print("Primer elemento:",datos[0])
    print("Último elemento:",datos[-1])
