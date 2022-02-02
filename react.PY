import requests, emoji, threading

chanid = 'channel id here'

with open('tokens.txt', 'r') as token:
  for line in token:
    token = line.rstrip('\n')

    def add_reaction(emoji):
      with open('message_ids.txt', 'r') as id:
         for line in id:
           id = line.rstrip('\n')
           r = requests.put(f'https://discord.com/api/v9/channels/{chanid}/messages/{id}/reactions/{emoji}/%40me', headers={    'Authorization': token    })      

    threading.Thread(target=add_reaction, args=(emoji.emojize(':thumbs_up:'))).start()
