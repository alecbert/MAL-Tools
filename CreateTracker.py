import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

#We could also check that the year isn't 18 but whatever
START_2018 = datetime(2018, 1, 1)

#This is all anime instead of just currently watching so I can see what I finished for this
r = requests.get('https://myanimelist.net/animelist/erg?status=7')
soup = BeautifulSoup(r.text, 'html.parser')

#idk if there will ever be more than 1 table that comes back for this
tables = soup.find_all('table', 'list-table')

#the list of everything that I'm watching/watched. json.loads makes it into a list
items = tables[0]['data-items']
jsonItems = json.loads(items)

#aggregator
epsLeft = 0

#printing all this out to a text file
with open('animeTracker.txt', 'w') as fileWriter:
    for x in jsonItems:
        if datetime.strptime(x['start_date_string'] or "01-01-18", '%m-%d-%y') < START_2018:
            #This is supposed to default to Jan 1 2018 for the finish date if one isn't in there, and we avoid this
            if datetime.strptime(x['finish_date_string'] or "01-01-18", "%m-%d-%y") > START_2018:
                print(x)
                fileWriter.write((x['anime_title'] + ' #' + str(x['anime_id']) + ' DONE!\n').encode('utf8'))
            else:
                fileWriter.write(x['anime_title'] + ' #' + str(x['anime_id']) + ' ' + str(x['num_watched_episodes']) + '/' + str(x['anime_num_episodes']) + '\n')
                epsLeft += (x['anime_num_episodes'] - x['num_watched_episodes'])
            
    fileWriter.write('\nEpisodes left ' + str(epsLeft))