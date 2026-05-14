"""
Extrae las imágenes más grandes de cada PDF para revisión visual.
Así podemos identificar qué imagen corresponde a qué producto.
"""
import os
from pypdf import PdfReader
from PIL import Image
import io

OUTPUT_DIR = r"C:\Users\USUARIO\PlazaSantaMaria\fotos_review"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Función para extraer la imagen más grande de un PDF en una página específica
def extract_largest_from_page(pdf_path, page_num, label, min_size=1000):
    reader = PdfReader(pdf_path)
    page = reader.pages[page_num]
    best = None
    best_size = min_size
    for img in page.images:
        if len(img.data) > best_size:
            best_size = len(img.data)
            best = img
    if best:
        ext = os.path.splitext(best.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png', '.jp2']:
            ext = '.png'
        out_path = os.path.join(OUTPUT_DIR, f"{label}{ext}")
        with open(out_path, 'wb') as f:
            f.write(best.data)
        print(f"  OK: {label}{ext} ({best_size} bytes, nombre original: {best.name})")
        return out_path
    else:
        print(f"  NO ENCONTRADA: {label}")
        return None

print("=== MUNDO JUEGOS ===")

# 10317 - 1 página, tiene 2 imágenes (logo y foto producto)
print("\n10317 (m1a, m1b, m1c):")
extract_largest_from_page(
    r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10317 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf",
    0, "10317_p1"
)

# 10318 - múltiples páginas con productos
print("\n10318 (m2a, m2b, m2c, m2d):")
mj18 = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10318 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"
for p in range(10):
    try:
        reader = PdfReader(mj18)
        page = reader.pages[p]
        imgs = page.images
        biggest = max(imgs, key=lambda x: len(x.data)) if imgs else None
        if biggest and len(biggest.data) > 50000:
            ext = os.path.splitext(biggest.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png', '.jp2']:
                ext = '.png'
            out_path = os.path.join(OUTPUT_DIR, f"10318_p{p+1}{ext}")
            with open(out_path, 'wb') as f:
                f.write(biggest.data)
            print(f"  Página {p+1}: {biggest.name} ({len(biggest.data)} bytes) -> 10318_p{p+1}{ext}")
    except:
        break

# 10319
print("\n10319 (m3a Velero Gigante):")
mj19 = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10319 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"
for p in range(9):
    try:
        reader = PdfReader(mj19)
        page = reader.pages[p]
        imgs = page.images
        biggest = max(imgs, key=lambda x: len(x.data)) if imgs else None
        if biggest and len(biggest.data) > 50000:
            ext = os.path.splitext(biggest.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png', '.jp2']:
                ext = '.png'
            out_path = os.path.join(OUTPUT_DIR, f"10319_p{p+1}{ext}")
            with open(out_path, 'wb') as f:
                f.write(biggest.data)
            print(f"  Página {p+1}: {biggest.name} ({len(biggest.data)} bytes) -> 10319_p{p+1}{ext}")
    except:
        break

# 10320
print("\n10320 (m4a Mangrullo Inclusivo Arbol):")
mj20 = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10320 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"
for p in range(9):
    try:
        reader = PdfReader(mj20)
        page = reader.pages[p]
        imgs = page.images
        biggest = max(imgs, key=lambda x: len(x.data)) if imgs else None
        if biggest and len(biggest.data) > 50000:
            ext = os.path.splitext(biggest.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png', '.jp2']:
                ext = '.png'
            out_path = os.path.join(OUTPUT_DIR, f"10320_p{p+1}{ext}")
            with open(out_path, 'wb') as f:
                f.write(biggest.data)
            print(f"  Página {p+1}: {biggest.name} ({len(biggest.data)} bytes) -> 10320_p{p+1}{ext}")
    except:
        break

# 10321
print("\n10321 (m5a Mangrullo Integrador 2T):")
mj21 = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10321 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"
for p in range(9):
    try:
        reader = PdfReader(mj21)
        page = reader.pages[p]
        imgs = page.images
        biggest = max(imgs, key=lambda x: len(x.data)) if imgs else None
        if biggest and len(biggest.data) > 50000:
            ext = os.path.splitext(biggest.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png', '.jp2']:
                ext = '.png'
            out_path = os.path.join(OUTPUT_DIR, f"10321_p{p+1}{ext}")
            with open(out_path, 'wb') as f:
                f.write(biggest.data)
            print(f"  Página {p+1}: {biggest.name} ({len(biggest.data)} bytes) -> 10321_p{p+1}{ext}")
    except:
        break

print("\n=== CRUCIJUEGOS ===")

# 36857 - 5 productos
print("\n36857 (c1a-c1e):")
cj57 = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos\Presupuesto-00236857-PDF.pdf"
reader = PdfReader(cj57)
for p in range(len(reader.pages)):
    imgs = reader.pages[p].images
    # Excluir imágenes pequeñas (logos, iconos)
    big_imgs = [i for i in imgs if len(i.data) > 30000]
    for j, img in enumerate(big_imgs):
        ext = os.path.splitext(img.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            ext = '.png'
        out_path = os.path.join(OUTPUT_DIR, f"36857_p{p+1}_i{j}{ext}")
        with open(out_path, 'wb') as f:
            f.write(img.data)
        print(f"  Página {p+1}, img {j}: {img.name} ({len(img.data)} bytes) -> {os.path.basename(out_path)}")

print("\n36858 (c2a):")
cj58 = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos\Presupuesto-00236858-PDF.pdf"
reader = PdfReader(cj58)
for p in range(len(reader.pages)):
    imgs = reader.pages[p].images
    big_imgs = [i for i in imgs if len(i.data) > 30000]
    for j, img in enumerate(big_imgs):
        ext = os.path.splitext(img.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            ext = '.png'
        out_path = os.path.join(OUTPUT_DIR, f"36858_p{p+1}_i{j}{ext}")
        with open(out_path, 'wb') as f:
            f.write(img.data)
        print(f"  Página {p+1}, img {j}: {img.name} ({len(img.data)} bytes) -> {os.path.basename(out_path)}")

print("\n36859 (c3a):")
cj59 = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos\Presupuesto-00236859-PDF.pdf"
reader = PdfReader(cj59)
for p in range(len(reader.pages)):
    imgs = reader.pages[p].images
    big_imgs = [i for i in imgs if len(i.data) > 30000]
    for j, img in enumerate(big_imgs):
        ext = os.path.splitext(img.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            ext = '.png'
        out_path = os.path.join(OUTPUT_DIR, f"36859_p{p+1}_i{j}{ext}")
        with open(out_path, 'wb') as f:
            f.write(img.data)
        print(f"  Página {p+1}, img {j}: {img.name} ({len(img.data)} bytes) -> {os.path.basename(out_path)}")

print("\nDone!")
