from instabot import Bot
from os import listdir
from os import getenv
from dotenv import load_dotenv

def upload_pictures(instagram_login, instagram_password, directory):
    bot = Bot()
    bot.login(username=instagram_login, password=instagram_password)
    pics = listdir(directory)
    for pic in pics:
        print(pic)
        filepath = directory + '/' + pic
        try:
            bot.upload_photo(filepath)
        except RuntimeError as e:
            print(e)    

def main():
    load_dotenv()
    instagram_login = getenv('INSTAGRAM_LOGIN')
    instagram_password = getenv('INSTAGRAM_PASSWORD')
    directory = 'images'
    upload_pictures(instagram_login, instagram_password, directory)    

if __name__ == '__main__':
    main()
