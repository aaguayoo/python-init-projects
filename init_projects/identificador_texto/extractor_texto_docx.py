def extraer_texto_pdf(archivo: str) -> str:
    import docx

    texto = docx.Document(archivo)
    return texto


# extraer_texto_pdf ("texto_prueba_doc.docx")
