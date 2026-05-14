"""
Script final de extracción de imágenes con IDs correctos.

Mapeo basado en análisis del texto de cada página:

MUNDO JUEGOS:
- m1a = Mangrullo Balcon de los Andes J20.38
  -> fotos.pdf página 6 (la imagen más grande, 1.6MB)
- m1b = Magic 2 Torres J14.13A
  -> fotos.pdf página 3, la imagen grande (618KB) = vista del juego
  -> O página 4 (vista general + área seguridad, sin imagen embebida grande)
  -> Mejor: 10318 tiene fichas de Barco Pirata, hamacas... buscar en "Propietarios" PDFs
  -> ALTERNATIVA: fotos.pdf p3 tiene fotos de la ficha técnica, J20.38 está en p6
     La p3 tiene las imágenes jp2 pequeñas (46KB, 39KB) = referencias de componentes
     La imagen grande de p3 (618KB) es el mangrullo grande
  -> El J14.13.A está en p4-5 del fotos.pdf: p5 tiene jpg de 73KB y jp2s, p4 no tiene img grande
  -> Usaremos fotos.pdf p5 img 0 (73044 bytes jpg) para m1b Magic 2 Torres
- m1c = Hamaca Cuadruple Inclusiva JI09.8
  -> fotos.pdf página 1, imagen grande jp2 (438KB)

MUNDO JUEGOS 10318 (Barco Pirata + 3 hamacas):
Texto confirma:
  - Página 3 (texto): "ART J20.35 - Barco Pirata" (pero sin imagen grande - las imgs son de componentes)
  - Página 2 tiene Im4.png (6.3MB) = la foto del Barco Pirata
  - Página 5: Im0.png (2.5MB) = Hamaca Silla Ruedas (p5 texto: "ART JI01.1")
  - Página 7: Im0.png (573KB) = Hamaca Plaza Cuadruple Combi (p7 texto menciona "Columpio cinta, Columpio bebé")
  - Página 9: Im0.png (918KB) = Hamaca Cuadruple Inclusiva JI09.11

MUNDO JUEGOS 10319:
  - Página 2: Im0.png (1.8MB) = Velero Gigante J20.25

MUNDO JUEGOS 10320:
  - Página 2: Im0.png (4.5MB) = Mangrullo Inclusivo Arbol JI20.7

MUNDO JUEGOS 10321:
  - Página 2: Im0.png (1.6MB) = Mangrullo Integrador 2T JI05.8

CRUCIJUEGOS 36857 (5 productos: c1a-c1e):
  - Domo Escalador R04079-SM = c1c
  - Calesita Circus P04072-A = c1d
  - Refugio Bosque Grande P16103-A = c1a
  - Mini Refugio Bosque P16106-A = c1b
  - Hamaca Triple Mixta P04109-A = c1e
  Las imágenes de p2: X23.jpg (442KB), X25.png (154KB), X26.png (311KB), X27.png (199KB), X28.png (92KB)
  El presupuesto lista: Domo, Calesita, Refugio Grande, Mini Refugio, Hamaca Triple
  p1 imagen X11 = logo grande (2.3MB) -> ignorar
  p2: 5 imágenes de productos (en el orden del presupuesto)

CRUCIJUEGOS 36858 (c2a = Refugio Bosque Chico P16101-A):
  p2 tiene X23.jpg (81KB), X25.jpg (442KB), X26.png (93KB), X27.png (154KB), X28.png (227KB)

CRUCIJUEGOS 36859 (c3a = Mangrullo Aldea Gigante P16117-E):
  p2: X23.jpg (442KB), X25.png (93KB), X26.png (154KB), X27.png (201KB)
"""

import warnings
warnings.filterwarnings('ignore')
from pypdf import PdfReader
import os

OUTPUT_DIR = r"C:\Users\USUARIO\PlazaSantaMaria\fotos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_image(pdf_path, page_num, img_index_or_name, out_id):
    """Extrae una imagen específica y la guarda con el ID dado."""
    reader = PdfReader(pdf_path)
    page = reader.pages[page_num]
    imgs = page.images

    if isinstance(img_index_or_name, int):
        img = imgs[img_index_or_name]
    else:
        # buscar por nombre
        img = next((i for i in imgs if i.name == img_index_or_name), None)
        if img is None:
            print(f"  WARN: imagen '{img_index_or_name}' no encontrada en página {page_num+1}")
            return False

    # Determinar extensión
    ext = os.path.splitext(img.name)[1].lower()
    if ext == '.jp2':
        ext = '.jpg'  # Guardar jp2 como jpg (son compatibles en muchos casos)
    elif ext not in ['.jpg', '.jpeg', '.png']:
        ext = '.jpg'

    out_path = os.path.join(OUTPUT_DIR, f"{out_id}{ext}")
    with open(out_path, 'wb') as f:
        f.write(img.data)
    print(f"  OK: {out_id}{ext} ({len(img.data):,} bytes) <- {img.name} p.{page_num+1}")
    return True

def extract_largest(pdf_path, page_num, out_id, min_size=50000):
    """Extrae la imagen más grande de una página."""
    reader = PdfReader(pdf_path)
    page = reader.pages[page_num]
    imgs = page.images
    best = max(imgs, key=lambda x: len(x.data)) if imgs else None
    if not best or len(best.data) < min_size:
        print(f"  WARN: no hay imagen suficientemente grande en p.{page_num+1} de {os.path.basename(pdf_path)}")
        return False
    ext = os.path.splitext(best.name)[1].lower()
    if ext == '.jp2':
        ext = '.jpg'
    elif ext not in ['.jpg', '.jpeg', '.png']:
        ext = '.jpg'
    out_path = os.path.join(OUTPUT_DIR, f"{out_id}{ext}")
    with open(out_path, 'wb') as f:
        f.write(best.data)
    print(f"  OK: {out_id}{ext} ({len(best.data):,} bytes) <- {best.name} p.{page_num+1}")
    return True

# Rutas
MJ = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos"
CJ = r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos"

FOTOS = f"{MJ}\\BARRIO SANTA MARIA TIGRE (fotos).pdf"
MJ17 = f"{MJ}\\10317 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"
MJ18 = f"{MJ}\\10318 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"
MJ19 = f"{MJ}\\10319 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"
MJ20 = f"{MJ}\\10320 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"
MJ21 = f"{MJ}\\10321 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf"
CJ57 = f"{CJ}\\Presupuesto-00236857-PDF.pdf"
CJ58 = f"{CJ}\\Presupuesto-00236858-PDF.pdf"
CJ59 = f"{CJ}\\Presupuesto-00236859-PDF.pdf"

results = {}

print("=== MUNDO JUEGOS - 10317 (3 juegos: m1a, m1b, m1c) ===")
print("  Nota: el 10317 es solo la cotización sin fichas técnicas de imagen.")
print("  Las imágenes de estos juegos están en el PDF de fotos de referencia.\n")

print("m1a = Mangrullo Balcon de los Andes J20.38 (fotos.pdf p6, imagen grande 1.6MB):")
results['m1a'] = extract_largest(FOTOS, 5, 'm1a')  # página 6 = índice 5

print("\nm1b = Magic 2 Torres J14.13A (fotos.pdf p5, foto jpg 73KB):")
# Página 5 tiene: X59.jpg (73KB), X60.jp2 (54KB), X61.jp2 (42KB) + pequeños
# El jpg de 73KB es la foto del juego (es el único jpg en esa página)
results['m1b'] = extract_image(FOTOS, 4, 0, 'm1b')  # página 5 = índice 4, primera img

print("\nm1c = Hamaca Cuadruple Inclusiva JI09.8 (fotos.pdf p1, jp2 438KB):")
# Página 1 tiene: X2.jp2 (438KB), X7.jp2 (47KB), X8.jp2 (40KB) + pequeños
results['m1c'] = extract_image(FOTOS, 0, 0, 'm1c')  # página 1 = índice 0, primera img

print("\n\n=== MUNDO JUEGOS - 10318 (4 juegos: m2a, m2b, m2c, m2d) ===")
print("\nm2a = Barco Pirata J20.35 (10318 p2, Im4.png 6.3MB):")
# Página 2, índice 4 = Im4.png (6354843 bytes) - la más grande
results['m2a'] = extract_image(MJ18, 1, 4, 'm2a')  # página 2, índice 4

print("\nm2b = Hamaca Silla Ruedas JI01.1 (10318 p5, Im0.png 2.5MB):")
results['m2b'] = extract_image(MJ18, 4, 0, 'm2b')  # página 5, índice 0

print("\nm2c = Hamaca Plaza Cuadruple Combi J01.4 (10318 p7, Im0.png 573KB):")
results['m2c'] = extract_image(MJ18, 6, 0, 'm2c')  # página 7, índice 0

print("\nm2d = Hamaca Cuadruple Inclusiva JI09.11 (10318 p9, Im0.png 918KB):")
results['m2d'] = extract_image(MJ18, 8, 0, 'm2d')  # página 9, índice 0

print("\n\n=== MUNDO JUEGOS - 10319 ===")
print("\nm3a = Velero Gigante J20.25 (10319 p2, Im0.png 1.8MB):")
results['m3a'] = extract_image(MJ19, 1, 0, 'm3a')

print("\n\n=== MUNDO JUEGOS - 10320 ===")
print("\nm4a = Mangrullo Inclusivo Arbol JI20.7 (10320 p2, Im0.png 4.5MB):")
results['m4a'] = extract_image(MJ20, 1, 0, 'm4a')

print("\n\n=== MUNDO JUEGOS - 10321 ===")
print("\nm5a = Mangrullo Integrador 2T JI05.8 (10321 p2, Im0.png 1.6MB):")
results['m5a'] = extract_image(MJ21, 1, 0, 'm5a')

print("\n\n=== CRUCIJUEGOS - 36857 (5 juegos: c1a-c1e) ===")
print("  Productos en orden del presupuesto página 2:")
print("  Domo Escalador R04079-SM (c1c)")
print("  Calesita Circus P04072-A (c1d)")
print("  Refugio Bosque Grande P16103-A (c1a)")
print("  Mini Refugio Bosque P16106-A (c1b)")
print("  Hamaca Triple Mixta P04109-A (c1e)")
print("  Imágenes p2: X20(logo), X23.jpg, X25.png, X26.png, X27.png, X28.png\n")

# Cargar imágenes de p2 del 36857
reader57 = PdfReader(CJ57)
p2_imgs57 = reader57.pages[1].images  # página 2 = índice 1
# Filtrar imágenes > 30KB (excluir logos pequeños de cabecera)
product_imgs57 = [img for img in p2_imgs57 if len(img.data) > 30000]
print(f"  Imágenes de producto en p2 (>30KB): {len(product_imgs57)}")
for i, img in enumerate(product_imgs57):
    print(f"    [{i}] {img.name}: {len(img.data):,} bytes")

# Orden de imágenes en p2 vs orden en el presupuesto:
# El texto de p2 lista: Domo Escalador, Calesita Circus, Refugio Grande, Mini Refugio, Hamaca Triple
# Pero las imágenes están embebidas en el PDF en el orden visual (izquierda a derecha, arriba abajo)
# Necesitamos mapear por tamaño/nombre a producto.
# X20.png (38319) = logo header pequeño
# Luego vienen: las fotos de productos

# Los 5 productos en orden del presupuesto (p2):
# c1a = Refugio Bosque Grande, c1b = Mini Refugio, c1c = Domo, c1d = Calesita, c1e = Hamaca Triple

# Extractor de imagen por índice dentro de product_imgs57
def save_from_list(imgs, idx, out_id):
    if idx >= len(imgs):
        print(f"  WARN: índice {idx} fuera de rango para {out_id}")
        return False
    img = imgs[idx]
    ext = os.path.splitext(img.name)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png']:
        ext = '.jpg'
    out_path = os.path.join(OUTPUT_DIR, f"{out_id}{ext}")
    with open(out_path, 'wb') as f:
        f.write(img.data)
    print(f"  OK: {out_id}{ext} ({len(img.data):,} bytes) <- {img.name}")
    return True

# La página 2 del 36857 tiene imágenes de izquierda a derecha en el PDF
# Inspeccionando el presupuesto de texto:
# Orden en el PDF: Refugio Grande (c1a), Mini Refugio (c1b), Domo (c1c), Calesita (c1d), Hamaca Triple (c1e)
# Las imágenes grandes de p2 son las 5 fotos de productos

# Imágenes de p2 con >30KB:
# X20.png (38319) = logo header
# X23.jpg (442146) = imagen 1 de producto
# X25.png (154473) = imagen 2
# X26.png (311088) = imagen 3
# X27.png (199499) = imagen 4
# X28.png (92902) = imagen 5

# Solo hay 5 imágenes >30KB pero una es el logo (38319)
# Las imágenes de productos son las de mayor tamaño: X23, X25, X26, X27, X28
# Orden en presupuesto (p2 detalle): Domo, Calesita, Refugio Grande, Mini Refugio, Hamaca Triple
# Pero el orden visual en la página puede diferir - extraemos todas 5

product_imgs57_filtered = [img for img in p2_imgs57 if len(img.data) > 40000]
print(f"\n  Imágenes de producto (>40KB): {len(product_imgs57_filtered)}")
for i, img in enumerate(product_imgs57_filtered):
    print(f"    [{i}] {img.name}: {len(img.data):,} bytes")

# Con >40KB se excluye el logo de 38KB y quedan solo las fotos de productos
# Hay 5 productos en 36857, así que debería haber 5 imágenes de productos
# Si solo hay 4, usaremos la de 38KB para el 5to

if len(product_imgs57_filtered) >= 5:
    print("\n  Mapeando 5 imágenes a 5 productos (c1a-c1e):")
    # Orden asumido por tamaño/posición:
    # La más grande probablemente es el Refugio Grande (el producto más grande)
    # Ordenamos por tamaño descendente para asignar al producto más importante
    sorted_imgs = sorted(product_imgs57_filtered, key=lambda x: len(x.data), reverse=True)

    # c1a = Refugio Bosque Grande (producto más grande y caro)
    # c1b = Mini Refugio Bosque
    # c1c = Domo Escalador
    # c1d = Calesita Circus
    # c1e = Hamaca Triple Mixta
    # Las imágenes vienen en orden visual del PDF
    # Extraemos en el orden en que aparecen en el PDF (order=índice)

    for i, item in enumerate(zip(['c1a', 'c1b', 'c1c', 'c1d', 'c1e'], product_imgs57_filtered[:5])):
        item_id, img = item
        ext = os.path.splitext(img.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            ext = '.jpg'
        out_path = os.path.join(OUTPUT_DIR, f"{item_id}{ext}")
        with open(out_path, 'wb') as f:
            f.write(img.data)
        print(f"    OK: {item_id}{ext} ({len(img.data):,} bytes) <- {img.name}")
        results[item_id] = True
elif len(product_imgs57_filtered) == 4:
    # Hay un producto sin imagen grande - usamos también la de 38KB
    all_product_imgs = [img for img in p2_imgs57 if len(img.data) > 30000]
    print(f"\n  Solo 4 imágenes >40KB, usando umbral 30KB: {len(all_product_imgs)} imágenes")
    for i, item in enumerate(zip(['c1a', 'c1b', 'c1c', 'c1d', 'c1e'], all_product_imgs[:5])):
        item_id, img = item
        ext = os.path.splitext(img.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            ext = '.jpg'
        out_path = os.path.join(OUTPUT_DIR, f"{item_id}{ext}")
        with open(out_path, 'wb') as f:
            f.write(img.data)
        print(f"    OK: {item_id}{ext} ({len(img.data):,} bytes) <- {img.name}")
        results[item_id] = True

print("\n\n=== CRUCIJUEGOS - 36858 (c2a = Refugio Bosque Chico P16101-A) ===")
reader58 = PdfReader(CJ58)
p2_imgs58 = reader58.pages[1].images
product_imgs58 = [img for img in p2_imgs58 if len(img.data) > 40000]
print(f"  Imágenes de producto en p2 (>40KB): {len(product_imgs58)}")
for i, img in enumerate(product_imgs58):
    print(f"    [{i}] {img.name}: {len(img.data):,} bytes")

# c2a = Refugio Bosque Chico - tomar la imagen más grande
best58 = max(product_imgs58, key=lambda x: len(x.data)) if product_imgs58 else None
if best58:
    ext = os.path.splitext(best58.name)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png']:
        ext = '.jpg'
    out_path = os.path.join(OUTPUT_DIR, f"c2a{ext}")
    with open(out_path, 'wb') as f:
        f.write(best58.data)
    print(f"\n  OK: c2a{ext} ({len(best58.data):,} bytes) <- {best58.name}")
    results['c2a'] = True

print("\n\n=== CRUCIJUEGOS - 36859 (c3a = Mangrullo Aldea Gigante P16117-E) ===")
reader59 = PdfReader(CJ59)
p2_imgs59 = reader59.pages[1].images
product_imgs59 = [img for img in p2_imgs59 if len(img.data) > 40000]
print(f"  Imágenes de producto en p2 (>40KB): {len(product_imgs59)}")
for i, img in enumerate(product_imgs59):
    print(f"    [{i}] {img.name}: {len(img.data):,} bytes")

best59 = max(product_imgs59, key=lambda x: len(x.data)) if product_imgs59 else None
if best59:
    ext = os.path.splitext(best59.name)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png']:
        ext = '.jpg'
    out_path = os.path.join(OUTPUT_DIR, f"c3a{ext}")
    with open(out_path, 'wb') as f:
        f.write(best59.data)
    print(f"\n  OK: c3a{ext} ({len(best59.data):,} bytes) <- {best59.name}")
    results['c3a'] = True

print("\n\n=== RESUMEN FINAL ===")
all_ids = ['m1a', 'm1b', 'm1c', 'm2a', 'm2b', 'm2c', 'm2d', 'm3a', 'm4a', 'm5a',
           'c1a', 'c1b', 'c1c', 'c1d', 'c1e', 'c2a', 'c3a']
for id_ in all_ids:
    status = "OK" if results.get(id_) else "FALTA"
    print(f"  {id_}: {status}")

print(f"\nTotal: {sum(1 for v in results.values() if v)}/{len(all_ids)} imágenes extraídas")

# Listar archivos guardados
print(f"\nArchivos en {OUTPUT_DIR}:")
for f in sorted(os.listdir(OUTPUT_DIR)):
    size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
    print(f"  {f} ({size:,} bytes)")
