from PIL import Image
import os
from glob import glob

img_dir = 'images'
for img_path in glob(f'{img_dir}/*'):
    img = Image.open(img_path)
    rgb_img = img.convert('RGB')
    new_path = os.path.splitext(img_path)[0] + '.jpg'
    rgb_img.save(new_path, 'JPEG')
    if img_path != new_path:
        os.remove(img_path)