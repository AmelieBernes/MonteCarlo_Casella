import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import random
import pylab

colores = ['#85a255', '#794775']

def generador_pk(n, p):
    """
    n y p son los parámetros de una Binomial
    Se regresa un array que contiene los valores p_k := P(X \leq k) para toda
    0 \leq k \leq n
    """
    q = 1-p
    valores_pk = [q**n] 
    for k in range(n):
        valores_pk.append(valores_pk[k] + scipy.special.binom(n, k+1) * p**(k+1) * (q)**(n-k-1))
    return valores_pk


def buscando(x, valores_pk, n):
    if x <= valores_pk[0]:
        return 0
    for k in range(1,n+1):
        if x > valores_pk[k-1] and x <= valores_pk[k]:
            return k
            

def muestreando_de_uniforme(n,p,N):
    """
    n y p son los parámetros de la binomial,
    N es la cantidad de muestras de una uniforme que vamos a usar para generar la binomial.
    """
    valores_pk = generador_pk(n,p)
    muestreo_uniforme = []
    for i in range(N):
        muestreo_uniforme.append(random.uniform(0,1))
    conteo = np.zeros(n+1) #contador de frecuencias
    for x in muestreo_uniforme:
        k = buscando(x, valores_pk, n)
        conteo[k] = conteo[k] + 1
    #print(conteo) #TODO sí está bien esto?
    return (1/N) * conteo #normalizamos para tener no los conteos netos, sino los porcentajes

def generando_binomial_de_uniforme(n, p, N):
    """
    n y p son los parámetros de la binomial
    N es la cant de números aleatorios generados en los dos experimentos
    """
    fig, axis = plt.subplots(1,2)
    fig.suptitle('Simulaciones de una distribución ' + r'$Bin({{{0}}})$'.format(str(n) + ', '+ str(p)) )

    # -----------------  PRIMERA SIMULACIÓN -------------------------
    
    valores_pk = generador_pk(n,p)
    conteo_porcentajes = muestreando_de_uniforme(n,p, N)
    for m in range(n+1):
        stemlines = axis[0].stem(m, conteo_porcentajes[m])
        plt.setp(stemlines, color = colores[0])
    axis[0].axhline(y=0, color = 'black') 
    axis[0].set_title('Binomial de Uniforme')

    # -----------------   SEGUNDA SIMULACIÓN -------------------------
    
    #generemos números de una binomial con parámetros n y p usando el generador de scipy
    conteo_binomial = np.zeros(n+1)
    for i in range(N):
        resultado = np.random.binomial(n, p) 
        conteo_binomial[resultado] += 1
    muestreo_binomial_porcentajes = (1/N)* conteo_binomial

    for m in range(n+1):
        stemlines = axis[1].stem(m, muestreo_binomial_porcentajes[m])
        plt.setp(stemlines, color = colores[1])
    axis[1].set_title('Binomial de scipy')


    for i in range(2):
        axis[i].grid()
        axis[i].axhline(y=0, color = 'black') 

    return plt.show()


if __name__ == '__main__': 
    generando_binomial_de_uniforme(10, 0.3, 10**4)
    #generando_binomial_de_uniforme(20, 0.3, 20000)


        
