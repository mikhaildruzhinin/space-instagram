import argparse
import requests
from save_pic import save_pic
from save_pic import crop_picture

def fetch_hubble_picture(image_id):
    image_id = str(image_id)
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url)
    response.raise_for_status()
    url = response.json()['image_files'][-1]['file_url'][2:]
    filename = url.split('/')[-1]
    file_id = url.split('/')[-2]
    url = f'https://hubblesite.org/uploads/image_file/image_attachment/{file_id}/{filename}'
    filename = save_pic('hubble', image_id, url, 'images')
    return filename

def download_hubble_collection(collection_title):
    url = f'http://hubblesite.org/api/v3/images/{collection_title}'
    response = requests.get(url)
    response.raise_for_status()
    collection = response.json()
    for item_number, item in enumerate(collection):
        image_id = collection[item_number]['id']
        filename = fetch_hubble_picture(image_id)
        crop_picture(filename)

def main():
    parser = argparse.ArgumentParser(description='Загрузка фотографий Hubble')
    parser.add_argument('collection_title', type=str, help='Название коллекции')
    args = parser.parse_args()
    collection_title = args.collection_title
    download_hubble_collection(collection_title)
    print(f'Коллекция {collection_title} сохранена')

if __name__ == '__main__':
    main()
