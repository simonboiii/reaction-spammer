import json, requests

token = input('Token to use for scraping')
chanid = input('Channel Id To Scrape All Message Ids: ')

def get_messages(channelid=chanid):
  r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers={    'Authorization': token    })
  jsonn = json.loads(r.text)
  for value in jsonn:
    print('Scraping Message Ids...')
    print(f"{value['id']} Scraped")
    with open('message_ids.txt', 'a') as scrape:
       scrape.write(value['id'] + '\n')

get_messages(chanid)