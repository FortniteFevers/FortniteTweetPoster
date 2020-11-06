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

#  Put your Twitter API keys and username here!

twitAPIKey = 'XXXXXXX'
twitAPISecretKey = 'XXXXXXX'
twitAccessToken = 'XXXXXXXXXXXXXX'
twitAccessTokenSecret = 'XXXXXXX'
username = 'XXXXXXX'

#-----------------------------------------------------------------------------------------#

auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
api = tweepy.API(auth)

print('\nWelcome to FortniteTweetPoster V1,',username+'!')
print('\nWhat do you want to tweet today?\n')
print('----------------------------------------------')
print("Supported lines:\n\nshop = Post Item Shop\nnewsbr = Post Battle Royale News\nText = lets you put in text to tweet\nversionbot = Starts the version bot\nleaks = Generates a new leaks image\nfrenzysue = let frenzy sue someone idk lol\ntajfam = tajfam or something #tajfam #tajnation")
print('newscr = Posts Creative News')
print('aes = Tweets current AES key!')
print('map = Tweets current Battle Royale map')
print('sizzy = its sizzy')
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
    api.update_with_media(f"shop.png", '#Fortnite Item Shop for '+str(d2)+'\n\nSupport-a-Creator Code: CEPTNITE10')
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
    api.update_with_media(f'leaks.jpg', '#Fortnite Leaks for current version.\n\nSupport-a-Creator Code: CEPTNITE10')
    print('News has been posted succesfully to Twitter!')
    print('Closing program...')
    time.sleep(2)
    exit()

# Exit:
if(text == 'exit'):
    print('\nExiting program....')
    time.sleep(1)
    exit()

if(text == 'sizzy'):
    print('\nAyo it sizzy leaks hi')
    time.sleep(5)

# Frenzy Sue:
if(text == 'frenzysue'):
    print('\nGood morning, Master Dave.')
    print('\nDo you want to sue today?')
    print('\nToday, your choices are Jinx, CyberDom, Nono, Sizzy, Thomas, or Fevers.\n')
    time.sleep(5)

# TajFam:
if(text == 'tajfam'):
    print('\nHey, taj here.')
    print('\nI sing songs by travis scott for some reason')
    print('\nAlso i am dating sizzy but dont tell anyone even doe its hella obvious')
    time.sleep(5)

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

# Map command thingey idk:
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
if(text == 'newsbr'):
    print("Running news for",username)
    api = tweepy.API(auth)
    api.update_with_media("news.gif", "#Fortnite News\n\nSupport-a-Creator Code: CEPTNITE10")
    print('News has been posted succesfully to Twitter!')
    print('Closing program...')
    time.sleep(2)
    exit()

# Text command
if(text == 'text'):
    print('\nWhat text do you want to tweet lil dude?\n')
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
            print('What do you want to tweet?')
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
