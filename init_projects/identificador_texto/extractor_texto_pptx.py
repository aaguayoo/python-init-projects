from pptx import Presentation
import glob


def extraer_texto_ppptx(archivo: str) -> str:
    for eachfile in glob.glob(archivo):
        prs = Presentation(eachfile)
        return archivo


extraer_texto_ppptx("texto_prueba_pptx.pptx")
