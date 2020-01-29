import argparse
import requests
from save_pic import save_pic
from save_pic import crop_picture

def fetch_spacex_launch(flight_number):
    url = 'https://api.spacexdata.com/v3/launches/'
    payload = {'flight_number': flight_number}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    urls = response.json()[0]['links']['flickr_images']
    for url_number, url in enumerate(urls):
        filename = save_pic(f'spacex_{flight_number}_', url_number, url, 'images')
        print(f'spacex_{flight_number}_{url_number} сохранён')
        crop_picture(filename)
    print('все фотографии запуска сохранены')

def main():
    parser = argparse.ArgumentParser(description='Загрузка фотографий запуска SpaceX')
    parser.add_argument('launch_number', type=int, help='Номер запуска')
    args = parser.parse_args()
    flight_number = args.launch_number # фотографии есть не у всех запусков, например 72, 73, 74, 81
    fetch_spacex_launch(flight_number)

if __name__ == '__main__':
    main()
