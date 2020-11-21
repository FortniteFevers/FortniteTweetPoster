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

twitAPIKey = 'XXXXXX'
twitAPISecretKey = 'XXXXXX'
twitAccessToken = 'XXXXXX'
twitAccessTokenSecret = 'XXXXXX'
username = 'XXXXXX'
sac = 'XXXXXX'

# Item Shop Config - leave both configs the same for default. Background urls are NOT supported.

textcolor = 'ffffff'
backgroundcolor = '1F1F1F'

# Current season - Put the current season here

#-----------------------------------------------------------------------------------------#

# Grabs twitter api keys from settings
auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
api = tweepy.API(auth)

#------------------
response = requests.get('https://pastebin.com/raw/i6UiYQX8')
print('\n------------')
print('Current updates:')
ln1 = response.json()["1"]
ln2 = response.json()["2"]
ln3 = response.json()["3"]
seasonend = response.json()["seasonend"]
currentseason = response.json()["currentseason"]
latestVersion = response.json()["currentVersion"]
print("")
print("")
print(ln1)
print(ln2)
print('------------')
#------------------

parsedseasonend = seasonend.split(", ")

seasoncountdown = datetime.date(int(parsedseasonend[0]), int(parsedseasonend[1]), int(parsedseasonend[2])) - datetime.date.today()

seasoncountdown = str(seasoncountdown)

# Starts the program and prints commands
print('\n\nWelcome to FortniteTweetPoster V1,',username+'!')
print('\nYou are on FTP version',latestVersion+'.')
print('\nWhat do you want to tweet today?\n')
print('----------------------------------------------')
print("Supported lines:\n\nshop = Posts Item Shop\nnews = Posts Battle Royale News\nText = lets you put in text to tweet\nversionbot = Starts the version bot\nleaks = Generates a new leaks image")
print('aes = Tweets current AES key!')
print('map = Tweets current Battle Royale map')
print('newscr = Posts Fortnite Creative News')
print('search = Searches for a cosmetic of your choice and tweets it.')
print('seasonbar = Grabs the current seasonbar and posts it to twitter.')
print('shopimage = Posts the shop image thing')
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

if(text == 'seasonbar'):
    print('\nRunning the season bar program for',username+'...')
    print('\nGrabbing how much days until the next season...')
    time.sleep(1)
    print('Grabbed the end date!')
    print('\nSeason '+str(currentseason)+' ends in ' +str(seasoncountdown.strip("0: ,"))+'!')
    print('\nSaving the image...')
    url = 'https://api.peely.de/v1/br/progress'
    r = requests.get(url, allow_redirects=True)
    open('progress.png', 'wb').write(r.content)
    print("\nOpened progress.png")
    print("\nSaved progress.png")
    print('\nDo you want to tweet the season bar?')
    barif = input ()
    if(barif == 'yes'):
        print('\nTweeting season bar. Give me around 5 seconds...')
        api = tweepy.API(auth)
        api.update_with_media(f'progress.png', 'Season '+str(currentseason)+' is ending in ' +str(seasoncountdown.strip("0: ,"))+'!'+'\n\n#Fortnite')
        print('\nThe season bar has been posted succesfully to Twitter!')
        print('Closing program...')
        time.sleep(2)
        exit()
    else:
        print('\nQuitting program...')
        time.sleep(3)
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
    print(f'\nThe current version v'+str(version)+'0'+' has been succesfully retrived!')
    print('The AES key, Paks, and Build have now been retreived also.')
    time.sleep(1)
    print('\nNow tweeting status to',username+'...')

    api.update_status('A #Fortnite update has been detected... \n\nVersion Number: v'+str(version)+'0'+'\n\nBuild: '+str(build)+':\n\n'+str(paks)+' - Pak Files\n\n'+str(dynamicpaks)+' - Dynamic Pak Files'+'\n\n'+str(aes)+' - AES key')
    print("The Fortnite Version has been succesfully tweeted to",username+'!')
    print('\nNow exiting program...')
    time.sleep(2)
    exit()

# Leaks:
if(text == 'leaks'):
    print("Running leaks for",username)
    url = 'https://i.ibb.co/CBh4z5h/14-60.png'
    r = requests.get(url, allow_redirects=True)
    open('14-60.png', 'wb').write(r.content)
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
    print:('Running the search cosmetics command.')
    print('\nWhich cosmetic do you want to export',username+'?\n')
    cosmetics = input()
    print('\nUser has asked for',cosmetics+'. Saving to computer now.')
    apiurl = 'https://fortnite-api.com/v2/cosmetics/br/search?name='+str(cosmetics)
    response = requests.get(apiurl)
    print("\nDetecting if there is a featured icon...")
    itemid = response.json()["data"]["id"]
    try:
        if response.json()["data"]["images"]["featured"] != None:
            print('\nA featured image has been detected!\nSaving featured icon...')
            url = response.json()["data"]["images"]["featured"]
            r = requests.get(url, allow_redirects=True)
            open(f'{itemid}.png', 'wb').write(r.content)
        else:
            print('\nA featured image has not been detected.\nSaving icon instead.')
            url = response.json()["data"]["images"]["icon"]
            print(url)
            r = requests.get(url, allow_redirects=True)
            open(f'{itemid}.png', 'wb').write(r.content)
    except:
        print("\nAn error has been detected.")
        print('The item:',cosmetics+' has not been found.')
        print('\nExiting program...')
        exit()
    url = 'https://fortnite-api.com/v2/cosmetics/br/search?name='+str(cosmetics)
    r = requests.get(url, allow_redirects=True)
    open('icon.png', 'wb').write(r.content)
    print('\nImage has been saved!')
    print('\nGetting cosmetic info...')
    response = requests.get('https://fortnite-api.com/v2/cosmetics/br/search?name='+str(cosmetics))
    itemname = response.json()["data"]['name']
    itemdesc = response.json()["data"]['description']
    itemrarity = response.json()["data"]['rarity']["value"]
    introduction = response.json()["data"]['introduction']["season"]
    print('Cosmetic info retreived! Printing icon details...')
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
        api.update_with_media(f'{itemid}.png', str(itemname)+':'+'\n\nDescription of '+str(itemname)+': \n'+str(itemdesc)+'\n\nItem Rarity: '+str(itemrarity)+'\n\nIntroduced in Season '+str(introduction))
        print("\nTweeted",itemname+' successfully to',username+'!')
    
# AES key:
if(text == 'aes'):
    print('\nGetting current AES.....\n')
    response = requests.get('https://benbotfn.tk/api/v1/aes')
    aes = response.json()['mainKey']
    response = requests.get('https://benbotfn.tk/api/v1/status')
    version = response.json()['currentFortniteVersionNumber']
    print("AES key has been succesfully retrived!\n")
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

# Runs the Shop Image bot
if(text == 'shopimage'):
    print('\nStarting the shop program...')
    api = tweepy.API(auth)
    print('\nTweeting the shop...')
    api.update_with_media(shopimage, '#Fortnite Item Shop for '+str(d2)+'\n\nSupport-a-Creator Code: '+str(sac))
    print('\nShop has been posted succesfully to Twitter!')
    print('\nClosing program...')
    time.sleep(2)
    exit()

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

            
