import copy
from PIL import Image
import colorsys
import random
import os
import itertools


# PASO 1: DEFINIMOS LA RUTA DE LA CARA BASE.
# PARA TODAS LAS RUTAS EN EL PROGRAMA PONDREMOS ANTES r SEGUIDO DE LA RUTA ENTRE COMILLAS:

cara_base = Image.open(r'C:\Users\fran2\Desktop\Programming\NFTS\Pruebas\base.png') #AQUÍ LA RUTA, DENTRO DEL PARÉNTESIS

'''
cara_base.show()
'''


'''CREAMOS UNA FUNCIÓN PARA OBTENER LA RUTA DE LAS IMAGENES EN CADA CARPETA:'''


def get_all_images(folder) :
    all_files = []
    '''Iterate through all files in folder'''
    for file in os.listdir(folder) :
        '''Get the file extension'''
        _, file_ext = os.path.splitext(file)
        full_file_path = os.path.join(folder, file)
        all_files.append(full_file_path)


    '''Get list of all files'''
    return all_files

# PASO 2: DEFINIMOS VARIABLE Y RUTA DE LAS CARPETAS DE CARACTERÍSTICAS
# (      EJEMPLO: ojos=(r"C:\Users\fran\Desktop\Programming\tokens\Pruebas\ojos")       )

ojos=(r"C:\Users\fran2\Desktop\Programming\NFTS\Pruebas\ojos")
bocas=(r"C:\Users\fran2\Desktop\Programming\NFTS\Pruebas\bocas")
narices=(r"C:\Users\fran2\Desktop\Programming\NFTS\Pruebas\narices")

# PASO 3: EJECUTAMOS LA FUNCIÓN CON CADA VARIABLE ( ESCRIBE   lista_x = get_all_images(x)  ) ( x = CADA CARACTERÍSTICA )

lista_ojos = get_all_images(ojos)
lista_bocas = get_all_images(bocas)
lista_narices = get_all_images(narices)

'''
print(lista_ojos)
'''

# PASO 4: INTRODUCIMOS, SEPARADAS POR UNA COMA, LAS VARIABLES ANTERIORES EN EL PARÉNTESIS INDICADO
'''CREAMOS LA LISTA DE COMBINACIONES UNICAS DE LAS RUTAS DE IMAGENES'''

combinaciones=[]
for combinacion in itertools.product(lista_bocas,lista_narices,lista_ojos): #AQUI SE INTRODUCEN LAS VARIABLES
    combinaciones.append(combinacion)


'''CUANTAS COMBINACIONES TENEMOS??? Y DE CUANTAS CARACTERISTICAS???'''

'''
print(len(combinaciones))
print(len(combinacion))
'''


'''CREAMOS DE NUEVO UNA LISTA CON TODOS LOS VALORES DE RUTA'''

lista1=[*range(0,len(combinaciones),1)]

lista2=[*range(0,len(combinacion),1)]


valores_ruta=[]
for valores in itertools.product(lista1,lista2):
    valores_ruta.append(valores)

'''
print(valores_ruta)
'''

'''JUNTAMOS NOMBRE E INDICE DE COMBINACIONES[0][0] (X EJEMPLO) CON DICCIONARIOS'''
'''F' SUSTITUYE AL .FORMAT EN UN STRING Y TE DA LA POSIBILIDAD DE PONER EL VALOR DENTRO DEL MISMO CORCHETE (EDDY)'''

nombre_indice = []
for indice in valores_ruta:
    x = indice[0]
    y = indice[1]
    valor = f'combinaciones[{x}][{y}]'
    nombre_indice.append(valor)

'''
print(nombre_indice)
'''

'''COMBINACIONES[0][0] SE CONVIERTE EN UN STRING TRAS PASAR A LA LISTA DE 'NOMBRE INDICE'. PARA ELIMINAR EL STRING >>>
>>> USAREMOS EVAL'''

'''
hola=Image.open(eval(nombre_indice[0]))
hola.show()
'''

'''DIVIDIMOS LOS ELEMENTOS DE NOMBRE_INDICE ENTRE LA LONGITUD DE LAS CARACTERISTICAS DE LA IMAGEN (len(combinacion))'''

lista_de_listas=[]
for i in range(0, len(nombre_indice), len(combinacion)):
    lista_de_listas.append(nombre_indice[i:i+len(combinacion)])

    '''
    print(nombre_indice[i:i+len(combinacion)])
print(lista_de_listas)
'''

'''TRAMO FINAL: COMPONEMOS LAS IMÁGENES'''

# PASO 5: DEFINIR LA RUTA DE CARPETA DESTINO DONDE SE GUARDEN LAS IMÁGENES COMPUESTAS.

new = cara_base.copy()
save_path = r'C:\Users\fran2\Desktop\Programming\NFTS\Pruebas\imagenes_guardadas' #AQUÍ SE PONE LA RUTA
i=0

for lista in lista_de_listas:
    lista=0
    for path in nombre_indice[i:i+len(combinacion)]:
        image = Image.open(eval(path))
        new.paste(image, (1,1), image)
        del image

        i+=1

# PASO 6: DEFINIMOS EN LA VARIABLE NAME_FILE EL NOMBRE DE NUESTRAS NUEVAS IMAGENES.
# ESTARÁN SEGUIDAS DE UN NÚMER0 (EJEMPLO: IMAGEN1.PNG, IMAGEN2.PNG, ETC)

    new.show() #PASO 7 OPCIONAL: PARA NO VER CÓMO SE ABRE CADA IMAGEN PON UN HASTAG DELANTE AQUÍ -> #new.show() .
    name_file = '\imagen' + str(int(i/(len(combinacion)))) + '.png' #AQUÍ SE CAMBIA EL NOMBRE
    new.save(save_path+name_file, 'png')
    lista+=1
    new.paste(cara_base)

# FIN
