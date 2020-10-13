import discord
import asyncio
from discord.ext import commands
import dndbot


bot = commands.Bot(command_prefix = '.')



@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command(name='shutdown')
async def shutdown(message):
    if str(message.author.id) == '275827627502075905':
        print('bot closed')
        await bot.close()
    else:
        print('unauthorized user ' + str(message.author.id + ' is trying to close the bot'))


@bot.command(name='commands')
async def user_commands(ctx):
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
    print('we made it to dice game function')
    await ctx.channel.send("type '1' to play against computer, '2' to wait for another player")
    choice = await bot.wait_for('message', check=lambda message: message.author == ctx.author)    
    if choice.content.lower() == '1':
        player = dndbot.roll_die(2, 6)
        computer = dndbot.roll_die(2, 6)
        await ctx.channel.send("You want to play with the computer")
        await ctx.channel.send(f"you rolled {player}")
        await ctx.channel.send(f"computer rolled {computer}")
        if computer > player:
            await ctx.channel.send("Computer Wins!")
        elif player > computer:
            await ctx.channel.send('Player Wins!')
    elif choice.content.lower() == '2':
        await ctx.channel.send("You want to play against another player")
        await ctx.channel.send(f"If you want to play against {ctx.author} type '1'")
        try:
            player2 = await bot.wait_for('message', check=lambda message: message.author != ctx.author, timeout = 20)
            if player2.content.lower() == '1':
                player_dice_total = dndbot.roll_die(2, 6)
                player2_dice_total = dndbot.roll_die(2, 6)
                await ctx.channel.send(f"{ctx.author} vs {player2.author}")
                await ctx.channel.send(f"{ctx.author}'s total: {player_dice_total}")
                await ctx.channel.send(f"{player2.author}'s total: {player2_dice_total}")
                if player_dice_total > player2_dice_total:
                    await ctx.channel.send(f"{ctx.author} wins!")
                elif player2_dice_total > player_dice_total:
                    await ctx.channel.send(f"{player2.author} wins!")

        except asyncio.TimeoutError:
            await ctx.channel.send('Sorry, no one wants to play with you!')

    

    

@bot.command(name='autocreate')
async def create_character(ctx):
    np = dndbot.AutoSelectPlayer()
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


@bot.command(name='combat')
async def combat(ctx):
    player1 = dndbot.AutoSelectPlayer()
    player1.set_attributes()
    await ctx.send(f'''
{ctx.author.id} your attributes are:
Strength: {player1.strength}
Dexterity: {player1.dexterity}
Constitution: {player1.constitution}
Intelligence: {player1.intelligence}
Wisdom: {player1.wisdom}
Charisma: {player1.charisma}
Press '1' to play against the computer or '2' to play against a friend.
                    ''')
    try:
        play_versus = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout = 20)
        if play_versus.content.lower() == '1':
            await ctx.send('play vs comp')
        elif play_versus == '2':
            pass #play vs friend
    except asyncio.TimeoutError:
        await ctx.send('Sorry, you took too long to respond')


    


bot.run('NzU3MzM0MTY0OTE0NzAwMzc5.X2e4Zw.5IR2Kwdd35YIE55YUSTQfRFmj1c')
