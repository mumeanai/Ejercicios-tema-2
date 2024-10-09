from datetime import date
from ejercicio2 import *

def muestra_variaciones_temperatura(ruta, fecha_inicial, fecha_final):
    variaciones = lee_variaciones_temperatura(ruta)
    
    #tendremos que dividir la lista de tuplasen dos
    
    valores_x =[]
    valores_y = []
    for v in variaciones:
        #if fecha_inicial <= v.fecha <= fecha_final: 
        if (fecha_inicial == None or v.fecha >= fecha_inicial)and\
            (fecha_final == None or v.fecha <= fecha_final): #filtros
            valores_x.append(v.fecha)
            valores_y.append(v.variacion)
    
    plt.title("variación de temperaturas medias del planeta")
    plt.plot(valores_x, valores_y)
    plt.show()
    
if __name__=="__main__":
    muestra_variaciones_temperatura("data/monthly_csv.csv", date(1880, 1, 1), date(2005, 1, 1))
    
    
    muestra_variaciones_temperatura("data/monthly_csv.csv", None, date(2005, 1, 1))
    
    muestra_variaciones_temperatura("data/monthly_csv.csv", date(1800, 1, 1), None)
