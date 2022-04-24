import typing

class SyncBotlistAPIResponse:
    def __init__(self,raw=None) -> None:
        self.status_code = raw.status_code
        self.content = raw.content
        self.res = raw
        self.json = raw.json()
        self.success = self.status_code < 400


class ItemStruct:
    def __init__(self):
        self.items = {}

    def from_object(self,obj:typing.Any):
        for item in list(obj.__dict__.keys()):
          if not item.startswith("__"):
            self.items[item] = obj.__dict__[item]

    @classmethod
    def from_json(cls,json):
        new = cls()
        for item in list(json.keys()):
            new[item] = json[item]

        return new


    def __getitem__(self,item):
        return self.items.get(item)
        
    def __setitem__(self,item,value):
        self.items[item] = value


class BotlistAPIResponse:
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

class Asset:
    def __init__(self,byte_data):
        self.bytes = byte_data
        
    def save(self,fp):
        with open(fp,"wb") as f:
            f.write(self.bytes)


    
class Bot(BotlistBaseUser):
    def __init__(self,id,**kwargs):
        super().__init__(id,kwargs)
