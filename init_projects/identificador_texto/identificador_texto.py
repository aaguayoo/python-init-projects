with open("semblanza.docx, r") as texto_analizar:
    lineas = texto_analizar.readlines()
    for linea in lineas:
        palabra = "la"
#find() method returns -1 if the value is not found
    if linea.find(palabra) != -1:
        print("Información contenida en el texto")
        print("Línea número: ", lineas.index(linea))



