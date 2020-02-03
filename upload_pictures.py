import os
from instabot import Bot
from dotenv import load_dotenv

def upload_pictures(instagram_login, instagram_password, directory):
    bot = Bot()
    bot.login(username=instagram_login, password=instagram_password)
    pics = os.listdir(directory)
    for pic in pics:
        if pic != '.DS_Store':
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
