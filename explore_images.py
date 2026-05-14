"""
Script de exploración: muestra cuántas imágenes hay por página en cada PDF.
"""
import sys
from pypdf import PdfReader

pdfs = {
    "MJ_fotos": r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\BARRIO SANTA MARIA TIGRE (fotos).pdf",
    "MJ_10317": r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10317 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf",
    "MJ_10318": r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10318 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf",
    "MJ_10319": r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10319 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf",
    "MJ_10320": r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10320 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf",
    "MJ_10321": r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10321 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf",
    "CJ_36857": r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos\Presupuesto-00236857-PDF.pdf",
    "CJ_36858": r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos\Presupuesto-00236858-PDF.pdf",
    "CJ_36859": r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos\Presupuesto-00236859-PDF.pdf",
}

for name, path in pdfs.items():
    print(f"\n=== {name} ===")
    try:
        reader = PdfReader(path)
        print(f"  Páginas: {len(reader.pages)}")
        for i, page in enumerate(reader.pages):
            imgs = page.images
            if imgs:
                print(f"  Página {i+1}: {len(imgs)} imagen(es)")
                for j, img in enumerate(imgs):
                    print(f"    [{j}] name={img.name}, len(data)={len(img.data)}")
    except Exception as e:
        print(f"  ERROR: {e}")
