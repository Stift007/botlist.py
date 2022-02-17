class BotlistAPIResponse:
    def __init__(self,raw=None) -> None:
        self.status_code = raw.status_code
        self.content = raw.content
        self.res = raw
        self.json = raw.json()
        self.success = self.status_code < 400

class SyncBotlistAPIResponse:
    def __init__(self,raw=None) -> None:
        self.status_code = raw.status
        self.content = raw.content
        self.res = raw
        self.success = self.status_code < 400


class Vote:
    def __init__(self,hasVoted:bool,timestamp):
        self.hasVoted = hasVoted
        self.timestamp = timestamp

class BotlistBaseUser:
    def __init__(self,id,json) -> None:
        self.id = id
        self.__dict__.update(**json)

    def __repr__(self) -> str:
        return f'abc.BotlistBaseUser:{self.id}'

    def __int__(self):
        return self.id

    def __str__(self):
        return self.__dict__

class Bot(BotlistBaseUser):
    def __init__(self,id,**kwargs):
        super().__init__(id,kwargs)