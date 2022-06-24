import discord
import os
import utils
import ffxivapi

from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot(debug_guilds=[587659892425228348])

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.slash_command(guild_ids=[587659892425228348], name = "searchcharacter", description = "Search for an FFXIV character")
async def searchcharacter(ctx, world: discord.Option(str), forename: discord.Option(str), surname: discord.Option(str)):
    character = await ffxivapi.search_character(world, forename, surname)
    if character is None:
        await ctx.respond(f'Could not find {forename} {surname} on server {world}')
        return

    character_info = await ffxivapi.get_character(character['ID'])
    if character_info is None:
        await ctx.respond(f'Could not find {forename} {surname} on server {world}')
        return

    embed= discord.Embed(
        title=character['Name'],
        color=discord.Colour.blurple()
    )
    embed.set_thumbnail(url=character['Avatar'])

    embed.add_field(name='Server', value=character['Server'], inline=False)
    embed.add_field(name='Main Job', value=character_info['Character']['ActiveClassJob']['UnlockedState']['Name'], inline=False)

    jobs = character_info['Character']['ClassJobs']
    for job in jobs[0:20]:
        level = int(job['Level'])
        if level == 90:
            textlevel = f'***{level}***'
        else:
            textlevel = str(level)
        embed.add_field(name=job['UnlockedState']['Name'], value=textlevel, inline=True)

    await ctx.respond(embed=embed)


bot.run(os.getenv('BOT_TOKEN'))