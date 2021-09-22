'Este  codigo  Calcula  e  imprime la sumatoria de riemman'
'Parametros  de  entredad :'
'n  =  el  número  de  veces  que  se  va  repetir  el  codigo'
'para  que la sumatoria sea mas exacta'
'Autor : Juan  Felipe  Corrales  Toro'
'ULTIMA  ACTUALIZACION : 22  de  Septiembre  /  2021'
import math # importamos la libraria math para tener una referencia de pi
n=float(input("ingresa el valor n que desees "))
def zeta(n): # defino la funcion zetaN para realizar el calculo de la sumatoria 
    k=1
    s=0
    i=1
    while n>=i: # use este while para realizar el ciclo de la sumatoria 
        suma=(1/(k**2)) # ecuacion del calculo
        k=k+1
        s=s+suma
        i=i+1
    return(s) # retornamos el valor final de la sumatoria 
p=zeta(n)
print("este es el resultado de tu sumatoria ",p)
cal=((math.pi**2)/6) # calculamos el valor de pi al cuadrado dividido seis 
e=cal-p # calculamos la diferencia entre cal y p
print("este es el resultado de la sumatoria original ",cal)
print("esta es la diferencia ",e)
