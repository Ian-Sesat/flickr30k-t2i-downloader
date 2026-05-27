"""
Flickr30k Download Script
Downloads Flickr30k from HuggingFace (lmms-lab/flickr30k).
Saves all 31,783 images and captions to disk.

Gallery : all images
Queries : all captions (5 per image)
"""

import os
import json
from datasets import load_dataset
from tqdm import tqdm

SAVE_DIR     = '/media/isesat/e8188905-1ffc-4de1-83b6-ac2addc2a941/flickr30k'
IMAGES_DIR   = os.path.join(SAVE_DIR, 'images')
CAPTION_FILE = os.path.join(SAVE_DIR, 'captions.json')

os.environ['HF_HOME'] = '/media/isesat/e8188905-1ffc-4de1-83b6-ac2addc2a941/hf_cache'
os.makedirs(IMAGES_DIR, exist_ok=True)

print("Downloading Flickr30k from HuggingFace...")
dataset = load_dataset('lmms-lab/flickr30k')
data    = dataset['test']
print(f"Images found: {len(data)}")

images  = []
queries = []
skipped = 0

for item in tqdm(data, desc="Saving"):
    img_id   = str(item['img_id'])
    captions = item['caption']
    filename = item['filename']

    img_path = os.path.join(IMAGES_DIR, filename)
    if not os.path.exists(img_path):
        try:
            item['image'].save(img_path)
        except Exception:
            skipped += 1
            continue

    images.append({'img_id': img_id, 'filename': filename})

    for caption in captions:
        queries.append({'img_id': img_id, 'caption': caption})

with open(CAPTION_FILE, 'w') as f:
    json.dump({'images': images, 'queries': queries}, f, indent=2)

print(f"Images saved  : {len(images):,}")
print(f"Skipped       : {skipped}")
print(f"Queries saved : {len(queries):,}")
print(f"Captions file : {CAPTION_FILE}")