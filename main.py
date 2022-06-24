import discord
import os
import utils
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot(debug_guilds=[587659892425228348])

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(guild_ids=[587659892425228348], name = "shame", description = "Shame Danneth")
async def shame(ctx):
    user = ctx.interaction.user
    await ctx.respond(f'<@185368034087665664> likes to succ {utils.user_to_ping(user)} a lot!')

bot.run(os.getenv('TOKEN'))