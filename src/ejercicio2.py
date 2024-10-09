from ejercicio1 import lee_variaciones_temperatura
from matplotlib import pyplot as plt #para generar una gráfica
#as es para poner un 

def muestra_variaciones_temperatura(ruta):
    variaciones = lee_variaciones_temperatura(ruta)
    
    #tendremos que dividir la lista de tuplasen dos
    
    valores_x =[]
    valores_y = []
    for v in variaciones:
        valores_x.append(v.fecha)
        valores_y.append(v.variacion)
    
    plt.title("variación de temperaturas medias del planeta")
    plt.plot(valores_x, valores_y)
    plt.show()
    
if __name__=="__main__":
    muestra_variaciones_temperatura("data/monthly_csv.csv")