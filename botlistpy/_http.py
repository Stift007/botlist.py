from fastapi import FastAPI
import typing
from .abc import ItemStruct

try:
    import orjson as _json
except ImportError:
    print("OrJson not found, using default json fallback...")
    import json as _json

router = FastAPI()

url_prefix = "/blme"
coroutine = None

@router.post("/test")
async def test():
    print("Booyah! It works!")
    return {
        'response':'kthxbye'
    }

@router.post(url_prefix)
async def test(json):
    print(json)
    try:
      await coroutine(ItemStruct.from_json(_json.loads(json)))
    except:
      await coroutine(json)
    return {"resp":True}
