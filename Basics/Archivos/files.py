archivo = open("test.txt",'r')
# print(archivo)
print(archivo.readlines())  # Lee el archivo y se queda en EOF
archivo.seek(0)        # Regresa a la primera linea
print(archivo.read())  # Vuelve a imprimir
archivo.close()

######## Para no tener que cerrar el archivo #######
try:
    with open('test.txt', mode='a') as miArchivo:
        texto = miArchivo.write('\n:)')
        #print(miArchivo.read())
except FileNotFoundError as err:
    print('El archivo no existe')
except IOError as err:
    print('No se pudo manejar el archivo')
####################################################

######### Para crear un archivo inexistente ########
with open('Carpeta/nuevo.txt', mode='w') as miArchivo2:
    texto = miArchivo2.write(':(((')
    #print(miArchivo.read())
####################################################