# Space Instagram

This project is a collection of three scripts. `fetch_spacex.py` downloads photos taken during the SpaceX rocket launch, `fetch_hubble.py` downloads photos taken by Hubble Space Telescope. `upload_pictures.py` can upload those pictures to your Instagram account, while `save_pic.py` doesn't do anything on its own, but rather gets imported into two fetch scripts.

## How to install

`upload_pictures.py` will not execute unless you have an [Instagran](https://www.instagram.com) account. Create a file with the name `.env` in the same directory with the script. Paste your login and password in the file:
```
INSTAGRAM_LOGIN='your login'
INSTAGRAM_PASSWORD='your password'
```
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## Launch

### fetch_spacex.py

```
python3 fetch_spacex.py number
```
where `number` is a number of the SpaceX launch. The script will create a folder called 'Images' in the same directory with the script and all of the pictures will be saved there.

### fetch_hubble.py

```
python3 fetch_hubble.py collection
```
where `collection` is a Hubble collection name. For information on different collections please read section Images of [Hubble API Documentation](http://hubblesite.org/api/documentation#images). This script works similarly to `fetch_spacex.py` and will use the same folder to store pictures.

### upload_pictures.py

```
python3 upload_pictures.py
```
This script uses [instabot](https://github.com/instagrambot/instabot) package and will upload every picture stored in the 'Images' folder.

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
