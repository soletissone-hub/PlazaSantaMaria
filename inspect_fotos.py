"""
Inspecciona el PDF de fotos de referencia y extrae todas las imágenes grandes.
También inspecciona qué contiene el PDF de fotos de Mundo Juegos.
"""
import warnings
warnings.filterwarnings('ignore')
from pypdf import PdfReader
import os

OUTPUT_DIR = r"C:\Users\USUARIO\PlazaSantaMaria\fotos_review"
os.makedirs(OUTPUT_DIR, exist_ok=True)

pdf_fotos = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\BARRIO SANTA MARIA TIGRE (fotos).pdf"

reader = PdfReader(pdf_fotos)
print(f"PDF de fotos: {len(reader.pages)} páginas")

# Extraer el texto de cada página para identificar qué juego está
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ''
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    print(f"\nPágina {i+1}:")
    for line in lines[:15]:
        print(f"  {line}".encode('ascii', errors='replace').decode())

    # Extraer imágenes grandes
    imgs = page.images
    big = [img for img in imgs if len(img.data) > 20000]
    for j, img in enumerate(big):
        ext = os.path.splitext(img.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png', '.jp2']:
            ext = '.jpg'
        outpath = os.path.join(OUTPUT_DIR, f"fotos_p{i+1}_i{j}{ext}")
        with open(outpath, 'wb') as f:
            f.write(img.data)
        print(f"  -> Guardada: fotos_p{i+1}_i{j}{ext} ({len(img.data)} bytes)")

print("\nDone!")
