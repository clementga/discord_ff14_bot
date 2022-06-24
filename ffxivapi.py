import asyncio
import aiohttp
import pyxivapi
import os

from dotenv import load_dotenv

load_dotenv()

async def search_character(world, forename, surname):
    client = pyxivapi.XIVAPIClient(api_key=os.getenv('API_KEY'))
    result = await client.character_search(world=world, forename=forename, surname=surname)
    await client.session.close()

    if not result['Results']: return None
    return result['Results'][0]

async def get_character(id):
    client = pyxivapi.XIVAPIClient(api_key=os.getenv('API_KEY'))
    result = await client.character_by_id(id)
    await client.session.close()

    if 'error' in result: return None
    return result

if __name__ == '__main__':
    result = asyncio.run(search_character('omega', 'storm', 'wyvern'))
    print(result)