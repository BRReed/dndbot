import discord
from discord.ext import commands
import dndbot

bot_object = commands.Bot(command_prefix = '.')



@bot_object.event
async def on_ready():
    print('Bot is ready.')

@bot_object.command(name='shutdown')
async def shutdown(message):
    if str(message.author.id) == '275827627502075905':
        await bot_object.close()
        print('bot closed')
    else:
        print('unauthorized user ' + str(message.author.id + ' is trying to close the bot'))


@bot_object.command(name='commands')
async def commands(ctx):
    await ctx.send(
        """
.dicegame
.commands - get a list of commands
.create - begin a character
.autocreate - auto create a character
.customcreate - customize a character
        
        """

    )

@bot_object.command(name='dicegame')
async def dice_game(message):
    author = str(message.author.id)
    print('we made it to dice game function')
    await message.channel.send(f"type .1 to play against computer, .2 to wait for another player{author}"
    )
    



@bot_object.command(name='autocreate')
async def create_character(ctx):
    np = dndbot.NonPlayer()
    np.set_attributes()
    np.print_attributes()
    await ctx.send(f'''
Strength: {np.strength}
Dexterity: {np.dexterity}
Constitution: {np.constitution}
Intelligence: {np.intelligence}
Wisdom: {np.wisdom}
Charisma: {np.charisma}
                    ''')

bot_object.run('NzU3MzM0MTY0OTE0NzAwMzc5.X2e4Zw.5IR2Kwdd35YIE55YUSTQfRFmj1c')
