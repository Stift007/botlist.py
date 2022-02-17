# Botlist.py
BotList.Py is a quick, asynchronous Wrapper around Botlist.me's API
Using BotList.Py is easy. I will give you a small Introduction how to use this Library.  

## Basics

BotList.py's actions are handled via BotClients. A BotClient holds all the methods, required  
to use the API:

### Creating a BotClient
A BotClient is easily created:
```py
from botlistpy import BotClient
botlist_client = BotClient(client_id,api_token)
```

### Your first request
Let's start by creating an EMBED for your Bot:
```py
img = await botlist_client.generate_embed()
with open("embed.png","wb") as f:
    f.write(img)
```

### Updating Bot Stats
The main part why you're using this Library, is propably because you  
want to set your Bot's Stats. Well, BotList.py makes this especially easy!

```py
server_count = 10
shard_count=1
await botlist_client.setStats(server_count,shard_count)
```

### AutoPosting
An essential part of the Library is the AutoPoster, a class that automatically updates Stats once per minute (or a custom interval)

```py
from botlistpy.helpers import AutoPoster
from mycoolbot import bot

poster = AutoPoster(botlist_client,bot,interval=45)
await poster.start()
```

### SyncBotClient
All of the Above Examples were ASYNC. However, async tasks are hard to handle  
in Python, so I gave it a shot and made the SyncBotClient - it works just like the [BotClient](#creating-a-botclient),  
but it's not async:

```py
from botlistpy.helpers import SyncBotClient
botlist_client = SyncBotClient(client_id,api_token)
```