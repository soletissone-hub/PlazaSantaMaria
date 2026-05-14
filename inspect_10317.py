"""
Inspecciona el PDF 10317 para ver si hay fichas de los 3 juegos en otra parte.
También extrae el texto completo de su única página.
"""
import warnings
warnings.filterwarnings('ignore')
from pypdf import PdfReader
import os

pdf = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10317 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"

# Intentar abrir con nombre literal
import glob
files = glob.glob(r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10317*")
print("Archivos encontrados:", files)

for f in files:
    print(f"\n=== {os.path.basename(f)} ===")
    try:
        reader = PdfReader(f)
        print(f"Páginas: {len(reader.pages)}")
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ''
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            print(f"\n  Página {i+1}:")
            for line in lines:
                print(f"    {line}".encode('ascii', errors='replace').decode())
    except Exception as e:
        print(f"Error: {e}")
