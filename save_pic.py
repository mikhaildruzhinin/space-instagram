import requests
import os
from pathlib import Path
from PIL import Image

def save_pic(filename, url_number, url, filepath):
    url_number = str(url_number)
    file_extension = fetch_file_extension(url)
    filename = f'{filename}{url_number}.{file_extension}'
    response = requests.get(url)
    response.raise_for_status()

    Path(filepath).mkdir(parents=True, exist_ok=True)
    filepath = Path('images') / Path(filename)

    with filepath.open('wb') as file:
        file.write(response.content)
    return filename

def fetch_file_extension(url):
    filename = url.split('/')[-1]
    file_extension = os.path.splitext(filename)[1]
    return file_extension

def crop_picture(filename):
    filepath = Path('images') / Path(filename)
    image = Image.open(filepath)
    min_size = min(image.width, image.height)
    coordinates = ( (image.width - min_size) / 2 , (image.height - min_size) / 2, image.width - (image.width - min_size) / 2 , image.height - (image.height - min_size) / 2)
    cropped = image.crop(coordinates)
    cropped.save(filepath)
    