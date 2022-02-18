"""
Created on Thu Feb 17 18:15:33 2022

SIGNAL TO QUANTIZATION NOISE RATIO

@author: Edwin Vera
"""

import numpy as np
import matplotlib.pyplot as plt


N=4;
amp=((2**N)/2);
f=1/6;

def h(x):  # Definicion de funcion seno
    return amp*(np.sin(2*(np.pi)*f*x))

x=np.linspace(0,6,1000)  #Frecuencia de muestreo adecuada

# ------------------Redondeo al más cercano----------------------------------


plt.figure(1)
plt.plot(x,h(x),label='Senal')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid()
plt.legend()

y=np.round_(h(x),0) #Redondeo al más cercano

plt.step(x,y, label='Muestreada')  # Graficacion de la señal escalonada

error=h(x)-y;

plt.plot(x,error, label='Error') #Graficación del error

snr=20*np.log10(amp/np.max((np.abs(error))));  ##Adquisicion del SNR
snr=np.fix(snr); #Redondeo del SNR

snr=str(snr); #Conversion a string
bits=str(N);  #Conversion a string

plt.title('Redondeo al mas Cercano Nbits:'+ bits + '  SNR: '+ snr) ##Impresion de strings en el titulo

# ------------------Redondeo haia abajo----------------------------------


plt.figure(2)
plt.plot(x,h(x),label='Seno')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Redondeo hacia abajo')
plt.grid()
plt.legend()

z=np.floor(h(x)) #Redondeo hacia abajo

plt.step(x,z,label='Muestreada')  # Graficacion de la señal escalonada

error=h(x)-z;

plt.plot(x,error, label='Error')  #Graficacion del error

snr=20*np.log10(amp/np.max((np.abs(error))));  ##Adquisicion del SNR
snr=np.fix(snr); #Redondeo del SNR

snr=str(snr); #Conversion a string
bits=str(N);  #Conversion a string

plt.title('Redondeo al mas Cercano Nbits:'+ bits + '  SNR: '+ snr) ##Impresion de strings en el titulo

# ------------------Redondeo haia arriba----------------------------------

plt.figure(3)
plt.plot(x,h(x),label='Seno')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Redondeo hacia arriba')
plt.grid()
plt.legend()

w=np.ceil(h(x)) #Redondeo hacia abajo

plt.step(x,w,label='Muestreada')  # Graficacion de la señal escalonada

error=h(x)-w;

plt.plot(x,error, label='Error')  #Graficacion del error

snr=20*np.log10(amp/np.max((np.abs(error))));  ##Adquisicion del SNR
snr=np.fix(snr); #Redondeo del SNR

snr=str(snr); #Conversion a string
bits=str(N);  #Conversion a string

plt.title('Redondeo al mas Cercano Nbits:'+ bits + '  SNR: '+ snr) ##Impresion de strings en el titulo




