#Librerias que se utlizzarna en el codigo
import numpy as np                      #Funciones Utilies
import matplotlib.pyplot as plt         #Graficos
from scypy.integrate import odeint      #Resuelve Ec. Diferenciales de primer grado

#Definiendo al pendulo
g = 9.81 # m/s^2 Gravedad de donde se encuentra el pendulo (Tierra)
l = 5.0  # m Longitud del pendulo
b = 0.0  # Coeficiente de Amortiguamiento (0 por que es simple)
c = g/l  # Definicion de constantes Para simplificar la Ec.Diferencial
theta = np.pi/3 # Angulo
vtheta= 0.0     # Velocidad Angular

