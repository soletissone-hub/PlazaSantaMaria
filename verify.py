import warnings; warnings.filterwarnings('ignore')
from PIL import Image
import os

fotos_dir = r'C:\Users\USUARIO\PlazaSantaMaria\fotos'
print('ID    | Archivo         | Dimensiones      | Formato  | Tamano')
print('-'*70)
for f in sorted(os.listdir(fotos_dir)):
    path = os.path.join(fotos_dir, f)
    size_kb = os.path.getsize(path) // 1024
    try:
        img = Image.open(path)
        name_id = f.split('.')[0]
        dims = str(img.size[0]) + 'x' + str(img.size[1])
        row = name_id.ljust(5) + ' | ' + f.ljust(15) + ' | ' + dims.ljust(16) + ' | ' + str(img.format).ljust(8) + ' | ' + str(size_kb) + ' KB'
        print(row)
    except Exception as e:
        print('ERROR ' + f + ': ' + str(e))
