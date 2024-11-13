def extraer_texto_txt(archivo: str) -> str:
    texto = archivo.read()
    return texto


# extraer_texto_txt(open("texto_prueba_txt.txt", "r"))
