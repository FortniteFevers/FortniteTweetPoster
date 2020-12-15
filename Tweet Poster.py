import tweepy
import time
import os
import subprocess
import requests
import PIL
import datetime
import json
from datetime import date
from PIL import Image

today = date.today()

# Program title :)
os.system("cls")
os.system(
    "TITLE FortniteTweetPoster / By Fevers")

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

# https://fortniteapi.io API key goes here (ONLY REPLACE THE XXXX PART):

headers = {
    'Authorization': 'XXXX'
}

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
leaksimage = response.json()['leaksurl']
print("")
print("")
print(ln1)
print(ln2)
print('------------')
#------------------

parsedseasonend = seasonend.split(", ")

seasoncountdown = datetime.date(int(parsedseasonend[0]), int(parsedseasonend[1]), int(parsedseasonend[2])) - datetime.date.today()

seasoncountdown = str(seasoncountdown)

#--------------------------------------------------------------------#

# Starts the program and prints commands
print('\nWelcome to FortniteTweetPoster V1,',username+'!')
print('\nYou are on FTP version',latestVersion+'.')
print('\nWhat do you want to tweet today?\n')
print('----------------------------------------------')
print("Supported lines:\n\n")
print('shop = Posts Item Shop')
print('news = Posts Battle Royale News')
print('Text = lets you put in text to tweet')
print('versionbot = Starts the version bot')
print('leaks = Generates a new leaks image')
print('aes = Tweets current AES key!')
print('map = Tweets current Battle Royale map')
print('newscr = Posts Fortnite Creative News')
print('search = Searches for a cosmetic of your choice and tweets it.')
print('seasonbar = Grabs the current seasonbar and posts it to twitter.')
print('staging = Posts the current staging servers to your twitter!')
print('sac = Starts the Support-A-Creator checker bot!')
print('itemids = Grabs the new and leaked item ids from the most recent update (MUST USE API)')
print('shopsections = Tweets out the current Fortnite shop sections.')
print('notices = Grabs the most recent Fortnite In-Game notice and posts it to Twitter')
print('tournaments = Grabs the most recnet Fortnite In-Game tournament and posts it to Twitter')
print('fortnitecrew = Grabs the current Fortnite Crew Bundle information and posts it to Twitter.')
print('stats = Grabs the stats of a Fortnite account, gets the info, and posts it to Twitter.')
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
    api.update_with_media(f"shop.png", '#Fortnite Item Shop for '+str(d2)+'\n\nSupport-a-Creator Code: '+str(sac))
    print('Shop has been posted succesfully to',username+'!')
    print('Now closing program.')
    time.sleep(5)
    exit()

# Staging Servers Command
if(text == 'staging'):
    print('\nStarting the staging server bot...')
    response = requests.get('https://api.peely.de/v1/staging')
    print('\nCollecting the staging number...')
    staging = response.json()['data']['staging']
    response = requests.get('https://benbotfn.tk/api/v1/status')
    version = response.json()['currentFortniteVersionNumber']
    print(f'\nThe current version staging number and version number has been succesfully retrived!')
    print('\nThe staging servers are on '+str(staging)+'.')
    print('\nDo you want to tweet the staging servers?')
    staginginput = input()
    if(staginginput == 'yes'):
        print('\nTweeting the current staging servers to',username+'.')
        api = tweepy.API(auth)
        api.update_status('#Fortnite Version Uptate:\n\nPatch v'+str(staging)+' has been added to the pre-release staging servers. Epic is currently testing this update version, and will most likely release within the upcoming week(s).')
        print('\nSuccesfully tweeted the staging servers to',username+'.')
        print('\n\nClosing program in 5 seconds...')
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
    print('\nDo you want to tweet out this? - y/n')
    ask = input ()
    if(ask == "y"):
        print('\nNow tweeting status to',username+'...')
        api.update_status('A #Fortnite update has been detected... \n\nVersion Number: v'+str(version)+'0'+'\n\nBuild: '+str(build)+':\n\n'+str(paks)+' - Pak Files\n\n'+str(dynamicpaks)+' - Dynamic Pak Files'+'\n\n'+str(aes)+' - AES key')
        print("The Fortnite Version has been succesfully tweeted to",username+'!')
        print('\nNow exiting program...')
        time.sleep(2)
        exit()
    else:
        print('Exiting program...')
        time.sleep(5)
        exit()

# Leaks:
if(text == 'leaks'):
    print("Running leaks for",username)
    r = requests.get(leaksimage, allow_redirects=True)
    print("\nOpened leaks.png")
    open('leaks.png', 'wb').write(r.content)
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
    print('\nGetting current AES...\n')
    response = requests.get('https://benbotfn.tk/api/v1/aes')
    aes = response.json()['mainKey']
    response = requests.get('https://benbotfn.tk/api/v1/status')
    version = response.json()['currentFortniteVersionNumber']
    print("AES key has been succesfully retrived!\n")
    print("Current AES key:")
    print(aes)
    time.sleep(1)
    print('\nDo you want to tweet out the current AES? - y/n')
    ask1 = input()
    if(ask1 == "y"):
        print("\nNow tweeting...")
        api.update_status('AES Key for version v'+str(version)+'0'+':\n\n'+str(aes))
        print("The AES key has been succesfully tweeted!")
        time.sleep(1)
    else:
        print("Closing program in 5 seconds....")
        time.sleep(5)
        exit()

# Runs the map bot
if(text == 'map'):
    print("\nStarting program...\n")
    response = requests.get('https://benbotfn.tk/api/v1/status')
    version = response.json()['currentFortniteVersionNumber']
    print("\nRetrived current version number.")
    print('\nDo you want to tweet out the map with or without names? w/wo')
    ask = input()
    if(ask == "w"):
        print('\nTweeting map WITHOUT NAMES to',username+'...')
        print('\nSaving map image...')
        url = 'https://media.fortniteapi.io/images/map.png?showPOI=true'
        r = requests.get(url, allow_redirects=True)
        open('map.png', 'wb').write(r.content)
        print("Opened map.png")
        img=Image.open('map.png')
        img=img.resize((1200,1200),PIL.Image.ANTIALIAS)
        img.save('smallmap.png')
        os.remove('map.png')
        api.update_with_media('smallmap.png', '#Fortnite Map Update (with names):\n\nBattle Royale map for v'+str(version)+'0')
        print("Image has been tweeted to",username+'!')
        time.sleep(2)
        print("Finnished program. Closing in 5 seconds.")
        time.sleep(5)
        exit()
    else:
        print('\nTweeting map WITH NAMES to',username+'...')
        print('\nSaving map image...')
        url = 'https://media.fortniteapi.io/images/map.png'
        r = requests.get(url, allow_redirects=True)
        open('map.png', 'wb').write(r.content)
        print("Opened map.png")
        img=Image.open('map.png')
        img=img.resize((1200,1200),PIL.Image.ANTIALIAS)
        img.save('smallmap.png')
        os.remove('map.png')
        api.update_with_media('smallmap.png', '#Fortnite Map Update:\n\nBattle Royale map for v'+str(version)+'0.')
        print("\nImage has been tweeted to",username+'!')
        time.sleep(2)
        print("Finnished program. Closing in 5 seconds.")
        time.sleep(5)
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
        print('\nQuitting program...\n')
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
        
if(text == 'sac'):
    print('\nrunning the sac checker bot...')
    print('\n----SUPPORT A CREATOR CODE CHECKER----')
    print('            Made by Fevers            ')

    print('\n\nWhat code do you want to lookup?')
    text = input()
    print('\nGrabbing status for code '+str(text)+'...')

    response = requests.get('https://fortnite-api.com/v2/creatorcode?name='+str(text))

    try:
        status = response.json()['data']['status']
        codename = response.json()['data']['code']
        print('\nStatus for your code has been sucesfully grabbed!')
        print('\nThe code '+str(codename)+' is '+str(status)+'!')   

        print('\nDo you want to grab the creator code ID?  -  y/n')
        id = input()
        if(id == 'y'):
            print('\nGrabbing ID for code',codename)
            codeid = response.json()['data']['account']['id']
            print('The ID has been succesfully grabbed!')
            print('\nThe ID for code '+str(codename)+' is '+str(codeid)+'.')
            print('\nDo you want to tweet the results? - y/n')
            sacresults = input()
            if(sacresults == 'y'):
                print('\nTweeting results now.')
                api.update_status('I just checked the Creator Code "'+str(codename)+'" and it is '+str(status)+'!')
                print('The results have been tweeted!')
            else:
                print('Quitting program...')
                time.sleep(5)
                exit()

        if(id == 'n'):
            print('\nExiting program...')
            time.sleep(5)
            exit()

    except:
        status = response.json()['status']
        error = response.json()['error']
        print('\nA status '+str(status)+' error has been detected!')
        print('\nERROR: '+str(error))
        print('\nExiting program in 5 seconds...')
        time.sleep(5)
        exit()
        
if(text == 'itemids'):
    print('\nStarting the leaked item ids bot!')
    print('\nGrabbing the current leaked item ids...')
    apiurl = 'https://fortnite-api.com/v2/cosmetics/br/new'
    response = requests.get(apiurl)
    #print('\n' + response.text)
    time.sleep(1)
    print("\nSucesfully loaded the api.")
    print('\nGrabbing item IDs...\n')
    for item in response.json()['data']["items"]:
        itemid2 = item["id"]
        print(itemid2)
    print('\nThe IDs have been succesfully grabbed! Feel free to copy them!')
    time.sleep(5)
    exit()

if(text == 'shopsections'):
    print('\n----FORTNITE SHOP SECTIONS BOT----')
    print('            By Fevers             ')

    print('\nGrabbing current shop sections...')
    response = requests.get('https://benbotfn.tk/api/v1/calendar')

    print('\nDo you want to grab sections 1 or sections 0?')
    ask = input()

    if(ask == "1"):
        print('\nUser has asked for Shop Sections (1)...\n')
        sections = ""
        for sectionStoreEnds in response.json()['channels']['client-events']['states'][1]['state']['sectionStoreEnds']:
            section2 = sectionStoreEnds
            sections += "• " + section2 + "\n"

        print(sections)
        print('Do you want to tweet the Shop Sections? - y/n')
        ss = input ()
        if(ss == 'y'):
            print('\nTweeting out the current shop sections...')
            api.update_status(f'#Fortnite Current Shop Sections:\n\n'+str(sections))
            print('Tweeted out the shop sections!')
        else:
            print('\nClosing program...')
            time.sleep(5)
            exit()
    else:
        print('\nUser has asked for Shop Sections (0)...\n')
        sections = ""
        for sectionStoreEnds in response.json()['channels']['client-events']['states'][0]['state']['sectionStoreEnds']:
            section2 = sectionStoreEnds
            sections += "• " + section2 + "\n"

        print(sections)
        print('Do you want to tweet the Shop Sections? - y/n')
        ss = input ()
        if(ss == 'y'):
            print('\nTweeting out the current shop sections...')
            api.update_status(f'#Fortnite Current Shop Sections:\n\n'+str(sections))
            print('Tweeted out the shop sections!')
        else:
            print('\nClosing program...')
            time.sleep(5)
            exit()
        
if(text == "notices"):
    print('\nGrabbing the most recent Fortnite In-Game notice...')

    response = requests.get('https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game')
    
    print('\nDo you want to grab V1 or V2? - 1/2')
    ask = input()
    if(ask == "1"):
        try:
            fullsection = response.json()['emergencynotice']['news']['messages'][0]
            title = response.json()['emergencynotice']['news']['messages'][0]['title']
            body = response.json()['emergencynotice']['news']['messages'][0]['body']

            print('\nGrabbed the most recent notice!')
            print('\n'+str(title)+'\n'+str(body))

            print('\nDo you want to tweet out this notice? - y/n')
            ask = input ()
            if(ask == "y"):
                print('Tweeting out the notice...')
                api.update_status('Most recent Fortnite Notice | #Fortnite\n\n'+str(title)+'\n'+str(body))

        except:
            print('\nThere is no active notice!')
    else:
        try:
            fullsection = response.json()['emergencynoticev2']['news']['messages'][0]
            title = response.json()['emergencynoticev2']['news']['messages'][0]['title']
            body = response.json()['emergencynoticev2']['news']['messages'][0]['body']

            print('\nGrabbed the most recent notice!')
            print('\n'+str(title)+'\n'+str(body))

            print('\nDo you want to tweet out this notice? - y/n')
            ask = input ()
            if(ask == "y"):
                print('\nTweeting out the notice...')
                api.update_status('Most recent Fortnite Notice | #Fortnite\n\n'+str(title)+'\n'+str(body))

        except:
            print('\nThere is no active notice!')
        
if(text == "tournaments"):
    print('\nStarting the tournament bot...')

    print('\nGrabbing the most recent tournament...')

    response = requests.get('https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game')

    name = response.json()['tournamentinformation']['tournament_info']['tournaments'][0]['long_format_title']

    date = response.json()['tournamentinformation']['tournament_info']['tournaments'][0]['schedule_info']

    desc = response.json()['tournamentinformation']['tournament_info']['tournaments'][0]['details_description']

    image = response.json()['tournamentinformation']['tournament_info']['tournaments'][0]['playlist_tile_image']

    print("\nSaving image...")
    r = requests.get(image, allow_redirects=True)
    open(f'{name}.png', 'wb').write(r.content)

    print("\nSaved image!")

    print('\nGrabbed the most recent tournament!')

    print('\nMost recent tournament: '+str(name))
    print('\nUntil: '+str(date))
    print('\nDescription: '+str(desc))

    print('\nDo you want to tweet this tournament? - y/n')
    ask = input()
    if(ask == "y"):
        print('\nTweeting the '+str(name)+'tournament to',username+'...')
        api.update_with_media(f'{name}.png',str(name)+':\n\nUntil '+str(date)+'\n\n'+str(desc)+'\n\n#Fortnite')
        print(f'\nTweeted to {username}!')
        print('\nExiting program...')
        time.sleep(5)
        exit()
    else:
        print('Closing program...')
        time.sleep(5)
        exit()
        
if(text == 'fortnitecrew'):
    print('Fortnite Crew Pack checker')

    print('\nStarting bot...\n')

    response = requests.get('https://fortnitecontent-website-prod07.ol.epicgames.com/content/api/pages/fortnite-game')

    desc = response.json()['subscription']['purchaseSubscriptionDetails']['skinDescription']

    print('This months Crew Pack: '+str(desc))

    print("\nSaving image...")
    url = response.json()['subscription']['currentRewards']['itemShopTileImageURL']
    r = requests.get(url, allow_redirects=True)
    open('fortnitecrew.png', 'wb').write(r.content)

    print("\nSaved image!")

    os.remove('fortnitecrew.png')

    print('\nDo you want to tweet this? - y/n')
    ask = input()
    if(ask == "y"):
        print('\nTweeting this months crew pack to '+str(username)+'...')
        api.update_with_media(f'fortnitecrew.png','This months #Fortnite Crew Bundle:\n\n'+str(desc))
        print(f'\nTweeted to {username}!')
        print('\nExiting program...')
        time.sleep(5)
        exit()
    else:
        print('\nClosing program...')
        time.sleep(5)
        exit()

if(text == 'stats'):
    print('\nStarting the user stats bot...')

    print('\nWhat name do you want to grab stats of?')
    name = input()

    try:
        response = requests.get('https://fortnite-api.com/v1/stats/br/v2?name='+str(name))

        main = response.json()['data']

        realname = main['account']['name']

        thing = main['battlePass']['level']

        overallstats = main['stats']['all']['overall']['score']

        kills = main['stats']['all']['overall']['kills']

        matches = main['stats']['all']['overall']['matches']

        winrate = main['stats']['all']['overall']['winRate']

        print(f'\nGrabbed stats for user "{realname}"')

        print(f'\n{realname} has a Battle Pass tier {thing}!\nTheir overall score is {overallstats}\nTheir overall kills is {kills}!\nTheir overall matches played is {matches}.\nTheir win-rate is {winrate}!')

        print('\nDo you want to tweet out this info? - y/n')
        ask = input()
        if(ask == "y"):
            print(f'Tweeting out the stats for {realname}...')
    except:
        print('\nAn error has occured!')
        status = response.json()['status']
        error = response.json()['error']
        print(f'\nStatus: {status}\nError: {error}')
        time.sleep(5)
