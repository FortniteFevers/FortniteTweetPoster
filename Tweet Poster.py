import tweepy
import time
import os
import subprocess
import requests
import PIL
import datetime
from datetime import date
from PIL import Image

today = date.today()

# Grabs current date, and puts it into Month, Day, Year
d2 = today.strftime("%B %d, %Y")
print("\nCurrent date:", d2)

#-----------------------------------------------------------------------------------------#

#  Put your Twitter API keys, username, and SAC here!

twitAPIKey = 'XXXXXXX'
twitAPISecretKey = 'XXXXXXX'
twitAccessToken = 'XXXXXXXXXXXXXX'
twitAccessTokenSecret = 'XXXXXXX'
username = 'XXXXXXX'
sac = 'XXXXXX'

#-----------------------------------------------------------------------------------------#

# Grabs twitter api keys from settings
auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
api = tweepy.API(auth)

# Starts the program and prints commands
print('\nWelcome to FortniteTweetPoster V1,',username+'!')
print('\nWhat do you want to tweet today?\n')
print('----------------------------------------------')
print("Supported lines:\n\nshop = Posts Item Shop\nnews = Posts Battle Royale News\nText = lets you put in text to tweet\nversionbot = Starts the version bot\nleaks = Generates a new leaks image")
print('aes = Tweets current AES key!')
print('map = Tweets current Battle Royale map')
print('exit = exit the program')
print('----------------------------------------------\n')
text = input ()

# If user wants to post the shop, then....
if(text == 'shop'):
    print("Running shop for FeversBot account.")
    url = 'https://api.nitestats.com/v1/shop/image?footer=Creator%20Code%3A%20CEPTNITE10'
    r = requests.get(url, allow_redirects=True)
    open('shop.png', 'wb').write(r.content)
    print("\nOpened shop.png")
    print("\nSaved shop.png")
    api = tweepy.API(auth)
    api.update_with_media(f"shop.png", '#Fortnite Item Shop for '+str(d2)+'\n\nSupport-a-Creator Code:',sac)
    print('Shop has been posted succesfully to',username+'!')
    print('Now closing program.')
    time.sleep(5)
    exit()

# VersionBot code!
if(text == 'versionbot'):
    response = requests.get('https://benbotfn.tk/api/v1/aes')
    aes = response.json()['mainKey']
    response = requests.get('https://benbotfn.tk/api/v1/status')
    version = response.json()['currentFortniteVersionNumber']
    build = response.json()['currentFortniteVersion']
    paks = response.json()['totalPakCount']
    dynamicpaks = response.json()['dynamicPakCount']
    time.sleep(1)
    print(f'\nThe current version v'+str(version)+'0'+' has been succesfully retrived!')
    time.sleep(1)
    print('The AES key, Paks, and Build have now been retreived also.')
    time.sleep(1)
    print('\nNow tweeting status to',username+'...')

    api.update_status('A #Fortnite update has been detected... \n\nVersion Number: v'+str(version)+'0'+'\n\nBuild: '+str(build)+':\n\n'+str(paks)+' - Pak Files\n\n'+str(dynamicpaks)+' - Dynamic Pak Files'+'\n\n'+str(aes)+' - AES key')
    time.sleep(5)
    print("The Fortnite Version has been succesfully tweeted to",username+'!')
    time.sleep(1)
    print('\nNow exiting program...')
    time.sleep(2)
    exit()

# Leaks:
if(text == 'leaks'):
    print("Running leaks for",username)
    api = tweepy.API(auth)
    api.update_with_media(f'leaks.jpg', '#Fortnite Leaks for current version.\n\nSupport-a-Creator Code:',sac)
    print('News has been posted succesfully to Twitter!')
    print('Closing program...')
    time.sleep(2)
    exit()

# Exit:
if(text == 'exit'):
    print('\nExiting program....')
    time.sleep(1)
    exit()

# AES key:
if(text == 'aes'):
    print('\nGetting current AES.....\n')
    response = requests.get('https://benbotfn.tk/api/v1/aes')
    aes = response.json()['mainKey']
    response = requests.get('https://benbotfn.tk/api/v1/status')
    version = response.json()['currentFortniteVersionNumber']
    print("AES key has been succesfully retrived!\n")
    time.sleep(1)
    print("Current AES key:")
    print(aes)
    time.sleep(1)
    print("\nNow tweeting...")
    api.update_status('AES Key for version v'+str(version)+'0'+':\n\n'+str(aes))
    print("The AES key has been succesfully tweeted!")
    time.sleep(1)
    print("Cloasing program in 5 seconds....")
    time.sleep(5)
    exit()

# Runs the map bot
if(text == 'map'):
    print("\nStarting program...\n")
    url = 'https://media.fortniteapi.io/images/map.png'
    r = requests.get(url, allow_redirects=True)
    open('map.png', 'wb').write(r.content)
    print("Opened map.png")
    response = requests.get('https://benbotfn.tk/api/v1/status')
    version = response.json()['currentFortniteVersionNumber']
    print("\nRetrived current version number.")
    img=Image.open('map.png')
    img=img.resize((1200,1200),PIL.Image.ANTIALIAS)
    img.save('smallmap.png')
    os.remove('map.png')
    print('\nTweeting image to',username+'...')
    api.update_with_media('smallmap.png', 'The Fortnite Map has been Updated!\nBattle Royale map for v'+str(version)+'0')
    print("Image has been tweeted to",username+'!')
    time.sleep(2)
    print("Finnished program. Closing in 5 seconds.")
    time.sleep(5)

# NewsBR:
if(text == 'news'):
        apiurl = 'https://fortnite-api.com/v2/news/br'
        print('Starting News Bot...')
        response = requests.get(apiurl)
        print("\nSaving image")
        url = response.json()["data"]["image"]
        r = requests.get(url, allow_redirects=True)
        open('feed.gif', 'wb').write(r.content)

        print("\nSaved image")

        today = date.today()
        d = today.strftime("%m/%d/%y")

        response = requests.get(apiurl)
        url = response.json()["data"]["image"]

        print('\nTweeting image...')
        api = tweepy.API(auth)
        api.update_with_media("feed.gif","#Fortnite News Update for "+str(d)+'\n\nSupport-a-Creator: '+str(sac))
        print("\nTweeted image to",username+'!')
        time.sleep(5)

# Text command
if(text == 'text'):
    print('\nWhat text do you want to tweet',username+'?\n')
    realtext = input()
    print("\nAre you sure you want to tweet this?\n")
    text = input ()
    if(text == 'yes'):
        api.update_status(realtext)
        print("\nTweeting...")
        print('User has tweeted the text succesfully.')
        time.sleep(1)
        print('\nYour Tweet "'+realtext+'" has been tweeted to',username+'!')
        time.sleep(1)
        print('\nDo you want to tweet something else?')
        maybetweet = input ()
    else:
        print('\nBro why you dissrespect me like dat im quitting now\n')
        time.sleep(2)
        exit()
        if(maybetweet == 'yes'):
            print('What text do you want to tweet',username+'?')
            textv2 = input ()
            api.update_status(textv2)
            print("\nTweeting...")
            print('User has tweeted the text succesfully.')
            time.sleep(1)
            print('\nYour Tweet "'+text+'" has been tweeted!')
        else:
            print('\nBro why you dissrespect me like dat im quitting now\n')
            time.sleep(3)
            exit()
