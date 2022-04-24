import json
import requests, aiohttp
from .abc import BotlistAPIResponse, Vote

class BotClient:
    def __init__(self,client_id,api_token:str or None=None) -> None:
        self.client_id = client_id
        self.api_key = api_token

    async def generate_embed(self):
        async with aiohttp.ClientSession() as cs:
            resp = await cs.get(f"https://api.botlist.me/api/v1/embed/{self.client_id}")
            
            return resp.content
            
    async def setStats(self,server_count=0,shard_count=0):
        async with aiohttp.ClientSession() as cs:
            headers = {
                "authorization":self.api_key
            }
            resp = await cs.post(f"https://api.botlist.me/api/v1/bots/{self.client_id}/stats",headers=headers,data={
                "shard_count":shard_count,
                "server_count":server_count
            })
            return BotlistAPIResponse(resp)

    async def _has_voted(self,userID):
        """Check if a User has Voted | **Do NOT use this Function, as it's complicated to use. Use .hasVoted() instead

        Args:
            userID (_int_): _Represents a User by ID_

        Returns:
            _BotlistAPIResponse_: _Represents an API Response_
        """
        async with aiohttp.ClientSession() as cs:
            headers = {
                "authorization":self.api_key
            }
            resp = await cs.post(f"https://api.botlist.me/api/v1/bots/{self.client_id}/voted",headers=headers,params={
                "userID":userID
            })
            

            return BotlistAPIResponse(resp)

    async def hasVoted(self,user_id):
        """
        Check if a User has voted.

        Args:
            user_id (_int_): _A Discord User ID_

        :return: -> abc.Vote
        """
        res = await self._has_voted(user_id)
        data = json.loads(str(res.content))
        return Vote(**data)
