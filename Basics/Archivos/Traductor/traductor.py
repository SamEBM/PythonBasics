from translate import Translator

traductor = Translator(to_lang="es")
try:
    with open('texto.txt', mode='r',encoding='utf-8') as archivo:
        contenido = archivo.read()
        traduccion = traductor.translate(contenido)
        with open('texto-es.txt', mode='w') as archivo2:
            archivo2.write(traduccion)
except FileNotFoundError as err:
    print('No se encontro el archivo')

