#EYPEspain sessions photos: https://imgur.com/a/xBiNfxp
import discord
import asyncio
from discord.ext import commands, tasks
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from itertools import cycle
from discord.utils import get
import json

client = commands.Bot(command_prefix = "!")
client.remove_command('help')
status = cycle(['🖥️Welcome to EYP','🏛️European Youth Parleament','🤖I hope you will enjoy this bot','💻Bot under development'])

# BOT CHECK
@client.event
async def on_ready():
    change_status.start()
    print('BOT ONLINE')

# STATUS
@tasks.loop(seconds=4)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# HELP COMMAND
@client.command(pass_context=True, aliases=['helpme', 'ajutor'])
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed( # MESAJ EMBED
         colour = discord.Colour.blue()
    )
    embed = discord.Embed(title="💡Available commands", colour=discord.Colour(0x8B59B6), description="The prefix is: `!`")
    embed.set_footer(text="The EYP Personal Bot is still in under development. For more informations contact the the owner.")
    embed.add_field(name="General commands", value="`help`,`sessions`", inline=False) #adaugat mai multe comenzi
    embed.add_field(name="Sessions commands", value="`Valencia`,`Barcelona`,`Madrid`,`Girona`,`Andalucía`,`Aragón`", inline=False)

    await ctx.send(embed=embed)

# CLEAR COMMAND
@client.command(aliases=['del', 'clean', 'purge', 'delete' ])
@has_permissions(manage_messages=True)
async def clear(ctx, amount):
    try: # VERIFICARE TEXT
        if(int(amount) <= 0): # VERIFICARE NUMAR POZITIV
            await ctx.send('You need to enter a pozitive number!')
        else: #VALOARE TRUE
            await ctx.channel.purge(limit=int(amount)+1) # STERGE MINIM 1 MESAJ
            await ctx.send('Messages deleted!', delete_after=3)
    except: # VERIFICARE IMPLICITA
        await ctx.send('Incorrect command! Example: !clear 5')
# CLEAR ERROR HANDLING
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You need to enter a value!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You cannot use this command!')

#----------------------------------------------------------------
#----------------------------------------------------------------


fileObject = open("/Users/Darius/Desktop/bot/token.txt", "r")
token = fileObject.read()

client.run(token)

