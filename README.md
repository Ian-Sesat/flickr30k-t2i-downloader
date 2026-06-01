# flickr30k-dataset-downloader

Downloads the Flickr30k dataset from HuggingFace for Text-to-Image retrieval evaluation. Saves all images to disk and exports a clean JSON file containing image filenames and captions ready for embedding extraction.

## Dataset

Flickr30k contains 31,783 images each annotated with 5 human-written captions, giving 158,915 text queries in total. Images were sourced from Flickr and cover a wide range of everyday scenes and activities.

## Usage

```bash
pip install datasets
```

## Output

```
flickr30k/
    images/          ← all 31,783 images saved as jpg
    captions.json    ← clean image and caption index
```

The captions.json file has two fields:

```json
{
    "images" : [{"img_id": "123", "filename": "123.jpg"}, ...],
    "queries": [{"img_id": "123", "caption": "A dog running in a field"}, ...]
}
```
