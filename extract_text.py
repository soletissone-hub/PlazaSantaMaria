"""
Extrae texto de cada página para identificar qué producto está en cada página.
"""
import warnings
warnings.filterwarnings('ignore')
from pypdf import PdfReader

def show_text(label, path, max_pages=None):
    print(f"\n{'='*60}")
    print(f"PDF: {label}")
    print('='*60)
    reader = PdfReader(path)
    pages = reader.pages if max_pages is None else reader.pages[:max_pages]
    for i, page in enumerate(pages):
        text = page.extract_text() or ''
        # Solo primeras líneas relevantes
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        print(f"\n  --- Página {i+1} ---")
        for line in lines[:20]:
            print(f"    {line}".encode('ascii', errors='replace').decode('ascii'))

show_text("10317", r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10317 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf")
show_text("10318", r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10318 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf")
show_text("10319", r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10319 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf")
show_text("10320", r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10320 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf")
show_text("10321", r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Mundo Juegos\10321 - CONS DE PROP AV. SANTA MARIA DE TIGRE Nº 6385.pdf")
show_text("36857", r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos\Presupuesto-00236857-PDF.pdf")
show_text("36858", r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos\Presupuesto-00236858-PDF.pdf")
show_text("36859", r"G:\Mi unidad\Soledad Tissone\Cotizaciones Plaza Santa Maria\Crucijuegos\Presupuesto-00236859-PDF.pdf")
