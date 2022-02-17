import json
import requests, aiohttp

from .core import BotClient
from .abc import SyncBotlistAPIResponse, Vote
import asyncio

class AutoPoster:
    def __init__(self,botclient:BotClient,discordHttpClient,interval:int=60) -> None:
        self.botclient = botclient
        self.discordClient = discordHttpClient
        assert interval >= 20, "Please choose a higher Interval to prevent Ratelimits"
        self.interval = interval

    async def start(self):
        while True:
            await self.botclient.setStats(len(self.discordClient.guilds),_approx_shards(self.discordClient))
            await asyncio.sleep(self.interval)
            
def _approx_shards(bot):
    if hasattr(bot,"shard_count"):
        return bot.shard_count
    return 1


class SyncBotClient:
    def __init__(self,client_id,api_token:str or None=None) -> None:
        """Like core.BotClient() but Sync

        """
        self.client_id = client_id
        self.api_key = api_token

    def generate_embed(self):
        
            resp = requests.get(f"https://api.botlist.me/api/v1/embed/{self.client_id}")
            
            return resp.content
            
    def setStats(self,server_count=0,shard_count=0):
            headers = {
                "authorization":self.api_key
            }
            resp = requests.post(f"https://api.botlist.me/api/v1/bots/{self.client_id}/stats",headers=headers,data={
                "shard_count":shard_count,
                "server_count":server_count
            })
            return SyncBotlistAPIResponse(resp)

    def _has_voted(self,userID):
        """Check if a User has Voted | **Do NOT use this Function, as it's complicated to use. Use .hasVoted() instead

        Args:
            userID (_int_): _Represents a User by ID_

        Returns:
            _BotlistAPIResponse_: _Represents an API Response_
        """
        headers = {
                "authorization":self.api_key
            }
        resp = requests.post(f"https://api.botlist.me/api/v1/bots/{self.client_id}/voted",headers=headers,params={
                "userID":userID
            })

        return SyncBotlistAPIResponse(resp)

    def hasVoted(self,user_id):
        """
        Check if a User has voted.

        Args:
            user_id (_int_): _A Discord User ID_

        :return: -> abc.Vote
        """
        res = self._has_voted(user_id)
        data = json.loads(str(res.content))
        return Vote(**data)