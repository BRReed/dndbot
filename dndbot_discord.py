import discord
from discord.ext import commands
import dndbot


bot = commands.Bot(command_prefix = '.')



@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command(name='shutdown')
async def shutdown(message):
    if str(message.author.id) == '275827627502075905':
        await bot.close()
        print('bot closed')
    else:
        print('unauthorized user ' + str(message.author.id + ' is trying to close the bot'))


@bot.command(name='commands')
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

@bot.command(name='dicegame')
async def dice_game(ctx):
    author = str(ctx.author.id)
    print('we made it to dice game function')
    await ctx.channel.send("type '1' to play against computer, '2' to wait for another player")
    choice = await bot.wait_for('message', check=lambda message: message.author == ctx.author)    
    if choice.content.lower() == 'a':
        await ctx.channel.send("You want to play with the computer")
        await ctx.channel.send(f"{dndbot.roll_die(2, 6)}")
    elif choice.content.lower() == 'b':
        await ctx.channel.send("You want to play against another player")
    

    

@bot.command(name='autocreate')
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

bot.run('NzU3MzM0MTY0OTE0NzAwMzc5.X2e4Zw.5IR2Kwdd35YIE55YUSTQfRFmj1c')
