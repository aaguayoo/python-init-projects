import fitz

def extraer_texto_pdf (archivo: str) -> str:
    with fitz.open(archivo) as doc:
        texto = ""
        for page in doc:
            texto += page.get_text()
    texto = texto.replace('�','')
    return texto
#extraer_texto_pdf ("texto_prueba_pdf.pdf")