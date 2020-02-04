import os
from instabot import Bot
from dotenv import load_dotenv
from save_pic import fetch_file_extension

def upload_pictures(instagram_login, instagram_password, directory):
    bot = Bot()
    bot.login(username=instagram_login, password=instagram_password)
    pics = os.listdir(directory)
    for pic in pics:
        file_extension = fetch_file_extension(pic)
        if file_extension == '.jpg' or file_extension == '.jpeg' or file_extension == '.png':
            filepath = os.path.join(directory, pic)
            try:
                bot.upload_photo(filepath)
            except RuntimeError:
                pass

def main():
    load_dotenv()
    instagram_login = os.getenv('INSTAGRAM_LOGIN')
    instagram_password = os.getenv('INSTAGRAM_PASSWORD')
    directory = 'images'
    upload_pictures(instagram_login, instagram_password, directory)    

if __name__ == '__main__':
    main()
