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
status = cycle(['🖥️Welcome to EYP','🏛️European Youth Parleament','🤖Enjoy the sessions!','💻Bot under development'])

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
    embed.add_field(name="General commands", value="`help`,`rules`,`sessions`", inline=False) #adaugat mai multe comenzi

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
@client.command()
async def rules(ctx):
    embed = discord.Embed( # MESAJ EMBED
         colour = discord.Colour.blue()
      )
    embed = discord.Embed(title="**Discord Server Rules**", color=0x0400f5)
    embed.add_field(name="1. Treat everyone with respect. Absolutely no harassment, witch hunting, sexism, racism, or hate speech will be tolerated.", value='|', inline=False)
    embed.add_field(name="2. Please do not spam channels.", value="|", inline=False)
    embed.add_field(name='3. Any kinds of illegal activity are forbidden.', value='|', inline=False)
    embed.add_field(name='4. If you need assistance, text any Technical Support Team Member.', value='|', inline=False)
    embed.add_field(name='5. Please tag "@" ethically, don’t unnecessarily spam .', value='|', inline=False)
    embed.add_field(name="6. Session language is English, so please don't spam in other languages.", value='|', inline=False)
    embed.add_field(name="7. Respect everyone’s privacy and do not share their personal information in public.", value='|', inline=False)
    embed.add_field(name="8. No NSFW or obscene content. This includes text, images, or links featuring nudity, sex, hard violence, or other graphically disturbing content.", value='|', inline=False)
    embed.add_field(name="9. If you see something against the rules or something that makes you feel unsafe, let the safe person  know. We want this server to be a welcoming space!", value='|', inline=False)
    embed.add_field(name="10. Please make sure that your nickname is Name, Role and Country (e.g. Alex (Orga, RO) )", value='@here', inline=False)
    embed.set_thumbnail(url="https://i.imgur.com/y9Dev9i.png")

    await ctx.send(embed=embed)

#----------------------------------------------------------------

@client.command(aliases=['valencia'])
async def Valencia(ctx):
    author = ctx.message.author

    embed = discord.Embed( # MESAJ EMBED
         title = 'Valencia RSC',
         description ="The session is from 19 February to 21 February",
         colour=discord.Colour.green()
    )
    embed.set_thumbnail(url="https://i.imgur.com/AlIhSrz.png")
    embed.set_footer(text="The EYP Personal Bot is still in under development. For errors contact the the owner.")

    await ctx.send(embed=embed)

@client.command(aliases=['barcelona'])
async def Barcelona(ctx):
    author = ctx.message.author

    embed = discord.Embed( # MESAJ EMBED
         title = 'Barcelona RSC and Northern Spain RSC',
         description ="The session is from 26 February to 28 February",
         colour=discord.Colour.red()
    )
    embed.set_thumbnail(url="https://i.imgur.com/5KEne4F.png")
    embed.set_footer(text="The EYP Personal Bot is still in under development. For errors contact the the owner.")

    await ctx.send(embed=embed)

@client.command(aliases=['madrid'])
async def Madrid(ctx):
    author = ctx.message.author

    embed = discord.Embed( # MESAJ EMBED
         title = 'Madrid RSC',
         description ="The session is from 5 March to 7 March",
         colour=discord.Colour(0x8B59B6)
    )
    embed.set_thumbnail(url="https://i.imgur.com/ZJj78Lj.png")
    embed.set_footer(text="The EYP Personal Bot is still in under development. For errors contact the the owner.")

    await ctx.send(embed=embed)

@client.command(aliases=['girona'])
async def Girona(ctx):
    author = ctx.message.author

    embed = discord.Embed( # MESAJ EMBED
         title = 'Baleares and Girona RSC',
         description ="The session is from 12 March to 14 March",
         colour=discord.Colour.dark_green()
    )
    embed.set_thumbnail(url="https://i.imgur.com/eiyHept.png")
    embed.set_footer(text="The EYP Personal Bot is still in under development. For errors contact the the owner.")

    await ctx.send(embed=embed)

@client.command(aliases=['Andalucía','andalucia','andalucía'])
async def Andalucia(ctx):
    author = ctx.message.author

    embed = discord.Embed( # MESAJ EMBED
         title = 'Andalucía RSC',
         description ="The session is from 5 March to 7 March",
         colour=discord.Colour(0xf1c40f)
    )
    embed.set_thumbnail(url="https://i.imgur.com/RDdzMHQ.png")
    embed.set_footer(text="The EYP Personal Bot is still in under development. For errors contact the the owner.")

    await ctx.send(embed=embed)

@client.command(aliases=['aragón', 'Aragon', 'aragon'])
async def Aragón(ctx):
    author = ctx.message.author

    embed = discord.Embed( # MESAJ EMBED
         title = 'Aragón RSC',
         description ="The session is from 26 March to 28 March",
         colour=discord.Colour(0xe67e22)
    )
    embed.set_thumbnail(url="https://i.imgur.com/qpEyYRR.png")
    embed.set_footer(text="The EYP Personal Bot is still in under development. For errors contact the the owner.")

    await ctx.send(embed=embed)


client.run('TOKEN')
