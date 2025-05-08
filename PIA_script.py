#Importamos librerías:
import re
import math
import openpyxl
from openpyxl import Workbook, load_workbook
from matplotlib import pyplot as plt

#Definimos media
def media(cont, lista_temperaturas):
    total = 0
    media_arit = 0
    for i in range(0,cont-1):
        total = total + lista_temperaturas[i]
        media_arit = total/cont
    return media_arit

#Definimos mediana
def mediana(cont):
    mitad = int(cont/2)
    izq = lista_temperaturas[mitad]
    der = lista_temperaturas[mitad-1]
    mediana_lista = (izq+der)/2
    return mediana_lista

#Definimos moda
def moda():
    diccionario_temperatura = {}
    for dato in lista_temperaturas:
        llave = str(dato)
        if not llave in diccionario_temperatura:
            diccionario_temperatura[llave] = 1
        else:
            diccionario_temperatura[llave] += 1
    freq = 0 
    muestra = str(lista_temperaturas[0])
    for elemento in diccionario_temperatura:
        if diccionario_temperatura[elemento] > freq:
            muestra = elemento
            freq = diccionario_temperatura[elemento]
    return muestra

#Definimos varianza
def varianza(cont, media_arit):
    primera = 0
    for i in range(cont):
        primera = primera + (lista_temperaturas[i] - media_arit)**2
    segunda = cont-1
    var = primera/segunda
    return var

def desv_est(var):
    estandar = math.sqrt(var)
    return estandar

#Extraemos la lista en str del archivo del modulo. 
archivo = open("C:\\Users\\andre\\OneDrive\\Documentos\\Paison\\prueba.txt", "r")
guardadito = archivo.read()
archivo.close()

#Buscamos los numeros con base en 'patron' y los convertimos a flotante con el for loop de 'numerote'
patron = r"\d{2}.\d|\d{1}.\d"
resultado = re.findall(patron, guardadito)

lista_temperaturas = []
cont = 0
for numerote in resultado:
    cont += 1
    lista_temperaturas.append(float(numerote))

#Iniciamos script y el archivo .xlsx (El archivo Excel)
book = load_workbook("C:\\Users\\andre\\OneDrive\\Documentos\\Paison\\procesado.xlsx")
sheet = book.active

media_arit = media(cont, lista_temperaturas)
mediana_lista = mediana(cont)
muestra = moda()
var = varianza(cont, media_arit)
estandar = desv_est(var)

#Guardamos cada valor en su casilla respectiva y el archivo .xlsx ya modificado
sheet['A2'].value = media_arit
sheet['B2'].value = mediana_lista
sheet['C2'].value = muestra
sheet['D2'].value = var
sheet['E2'].value = estandar
book.save("C:\\Users\\andre\\OneDrive\\Documentos\\Paison\\respuesta.xlsx")

#De momento mostramos los resultados
print("Temperatura con mayor frecuencia: {}".format(muestra))
print("Mediana de la temperatura: {}".format(mediana_lista))
print("Media de las temperaturas: {:.2f}".format(media_arit))
print("Varianza: {:.2f}".format(var))
print("Desviación estándar: {:.2f}".format(estandar))

#Graficamos y rotulamos
x = list(range(cont))
y = lista_temperaturas
plt.bar(x,y)
plt.xlabel('Numero de día')
plt.ylabel('Temperatura en °C')
plt.show()
#C:\\Users\\andre\\OneDrive\\Documentos\\Paison\\prueba.txt"
