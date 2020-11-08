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

# Item Shop Config - leave both configs the same for default. Background urls are NOT supported.

textcolor = 'ffffff'
backgroundcolor = '1F1F1F'

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
print('search = Searches for a cosmetic of your choice and tweets it. (WIP)')
print('exit = exit the program')
print('----------------------------------------------\n')
text = input ()

# If user wants to post the shop, then....
if(text == 'shop'):
    print("Running shop for",username)
    url = 'https://api.nitestats.com/v1/shop/image?footer=Creator%20Code%3A%20'+str(sac)+'&textcolor='+str(textcolor)+'&background='+str(backgroundcolor)
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
    url = 'https://i.ibb.co/Vpc0gsx/leaks.jpg'
    r = requests.get(url, allow_redirects=True)
    open('leaks.png', 'wb').write(r.content)
    print("\nOpened leaks.png")
    print("\nSaved leaks.png")
    print('\nDo you want to tweet out the leaks to twitter?\n')
    searchleaks = input()
    if(searchleaks == 'yes'):
        print('Tweeting leaks. Give me around 5 seconds...')
        api = tweepy.API(auth)
        api.update_with_media(f'leaks.png', '#Fortnite Leaks for current version.\n\nSupport-a-Creator Code:'+str(sac))
        print('\nLeaks have been posted succesfully to Twitter!')
        print('Closing program...')
        time.sleep(2)
        exit()
    else:
        print('\nNot tweeting leaks.')
        print('Closing program...')

# Exit:
if(text == 'exit'):
    print('\nExiting program....')
    time.sleep(1)
    exit()
   
# Search
if(text == 'search'):
    print('\nWhich cosmetic do you want to export',username+'?\n')
    cosmetics = input()
    print('\nUser has asked for',cosmetics+'. Saving to computer now.')
    apiurl = 'https://fortnite-api.com/v2/cosmetics/br/search?name='+str(cosmetics)
    response = requests.get(apiurl)
    print("\nSaving image")
    try:
        url = response.json()["data"]["images"]["icon"]
    except:
        print("\nAn error has been detected.")
        time.sleep(1)
        print('The item:',cosmetics+'has not been found.')
        print('\nExiting program...')
        time.sleep(2)
        exit()
    r = requests.get(url, allow_redirects=True)
    open('icon.png', 'wb').write(r.content)
    print('Image saved.')
    time.sleep(1)
    print('\nGetting icon info...')
    response = requests.get('https://fortnite-api.com/v2/cosmetics/br/search?name='+str(cosmetics))
    itemname = response.json()["data"]['name']
    itemdesc = response.json()["data"]['description']
    itemrarity = response.json()["data"]['rarity']["value"]
    introduction = response.json()["data"]['introduction']["season"]
    print('Icon info retreived! Printing icon details...')
    print('\nItem Details:')
    print('\nItem Name:',itemname)
    print('\nItem Description:',itemdesc)
    print('\nItem Rarity:',itemrarity)
    print('\nIntroduced in season',introduction)
    print('\nDo you want to tweet out',itemname+'?\n')
    searchin = input()
    if(searchin == 'yes'):
        print('\nTweeting out',itemname+'.')
        api = tweepy.API(auth)
        api.update_with_media("icon.png", str(itemname)+':'+'\n\nDescription of '+str(itemname)+': \n'+str(itemdesc)+'\n\nItem Rarity: '+str(itemrarity)+'\n\nIntroduced in season '+str(introduction))
        print("\nTweeted",itemname+' successfully to',username+'!')
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
        
# NewsCR:
if(text == 'newscr'):
        apiurl = 'https://fortnite-api.com/v2/news/creative'
        print('Starting News Bot for creative...')
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
        api.update_with_media("feed.gif","#Fortnite Creative News Update for "+str(d)+'\n\nSupport-a-Creator: '+str(sac))
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
