import discord
import asyncio
from discord.ext import commands
import dndbot
import dndbot_token


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
        print('unauthorized user ' + str(message.author.id) +
              ' is trying to close the bot')

# available commands in discord
@bot.command(name='commands')
async def user_commands(ctx):
    await ctx.send(
        """
**.dicegame** - Whoever rolls higher wins
**.commands** - Get a list of commands
**.create** - Make a character
**.load** - Load an already created character


        """
    )

# simple dice game used to test different aspects of the discord api
@bot.command(name='dicegame')
async def dice_game(ctx):
    print('we made it to dice game function')
    await ctx.channel.send("type '1' to play against computer,"+
                           "'2' to wait for another player")
    choice = await bot.wait_for('message',
            check=lambda message: message.author == ctx.author)
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
        await ctx.channel.send(
            "You want to play against another player")
        await ctx.channel.send("If you want to play against"+
                              f" {ctx.author} type '1'")
        try:
            player2 = await bot.wait_for('message',
                check=lambda message: message.author != ctx.author,
                timeout = 20)
            if player2.content.lower() == '1':
                player_dice_total = dndbot.roll_die(2, 6)
                player2_dice_total = dndbot.roll_die(2, 6)
                await ctx.channel.send(
                    f"{ctx.author} vs {player2.author}")
                await ctx.channel.send(f"{ctx.author}'s total:"+
                                       f" {player_dice_total}")
                await ctx.channel.send(f"{player2.author}'s total:"
                                       f" {player2_dice_total}")
                if player_dice_total > player2_dice_total:
                    await ctx.channel.send(f"{ctx.author} wins!")
                elif player2_dice_total > player_dice_total:
                    await ctx.channel.send(f"{player2.author} wins!")

        except asyncio.TimeoutError:
            await ctx.channel.send('''
Sorry, no one wants to play with you!
''')

# load a character that was already created by user's discord ID
@bot.command(name='load')
async def load_character(ctx):
    pass


# create a new character for dnd combat tied to user's discord ID
@bot.command(name='create')
async def create_character(ctx):
    await ctx.send(f'''
Enter '**1**' for **Barbarian**
Enter '**2**' for **Fighter**
Enter '**3**' for **Monk**
Enter '**4**' for **Paladin**
Enter '**5**' for **Rogue**
                    ''')

    player_class_choice = await bot.wait_for('message',
            check=lambda message: message.author == ctx.author,
            timeout = 20)
    player_create = dndbot.Character()
    if player_class_choice.content.lower() == '1':
        player_create.set_char_class('Barbarian')
    elif player_class_choice.content.lower() == '2':
        player_create.set_char_class('Fighter')
    elif player_class_choice.content.lower() == '3':
        player_create.set_char_class('Monk')
    elif player_class_choice.content.lower() == '4':
        player_create.set_char_class('Paladin')
    elif player_class_choice.content.lower() == '5':
        player_create.set_char_class('Rogue')
    else:
        print('Error in player_class_choice')
    await ctx.send(f'''
Enter '**1**' for **Dwarf**
Enter '**2**' for **Elf**
Enter '**3**' for **Human**
                    ''')

    player_race_choice = await bot.wait_for('message',
            check=lambda message: message.author == ctx.author,
            timeout = 20)
    if player_race_choice.content.lower() == '1':
        player_create.set_char_race('Dwarf')
    elif player_race_choice.content.lower() == '2':
        player_create.set_char_race('Elf')
    elif player_race_choice.content.lower() == '3':
        player_create.set_char_race('Human')
    player_create.set_attribute_modifier()
    await ctx.send(f'''
**{ctx.author.name}** has created a **{player_create.char_race} '''+
f'''{player_create.char_class}**

with proficiencies in: {player_create.print_proficiencies}

What weapon would you like to use:
Enter '**1**' for **Battleaxe**
Enter '**2**' for **Longsword**
Enter '**3**' for **Warhammer**
                    ''')

    player_weapon_choice = await bot.wait_for('message',
            check=lambda message: message.author == ctx.author,
            timeout = 20)
    if player_weapon_choice.content.lower() == '1':
        player_create.set_char_weapon('Battleaxe')
    elif player_weapon_choice.content.lower() == '2':
        player_create.set_char_weapon('Longsword')
    elif player_weapon_choice.content.lower() == '3':
        player_create.set_char_weapon('Warhammer')
    while True:
        try:
            await ctx.send(f'''
**What is your character's name?**
* No special characters
* Shorter than 30 characters
                ''')

            characters_name = await bot.wait_for('message',
                check=lambda message: message.author == ctx.author,
                timeout = 360)

            if player_create.set_char_name(
                characters_name.content.lower()) == False:
                continue
            elif player_create.set_char_name(
                characters_name.content.lower()) == True:
                break
        except asyncio.TimeoutError:
            await ctx.send('''You have timed out,'''+
                           ''' please recreate your character''')
            break

    await ctx.send(f'''
**{player_create.name}** the **{player_create.char_class}'''+
f''' {player_create.char_race}** has been created
Enter '**1**' to save **{player_create.name}**
Enter '**2**' to delete **{player_create.name}**
    ''')

    character_save = await bot.wait_for('message',
            check=lambda message: message.author == ctx.author,
            timeout = 60)
    if character_save.content.lower() == '1':
        player_create.save_char_info(ctx.author.id)
        await ctx.send(f'''
**{player_create.name}** has been saved!
You can now engage in combat against the computer or another player!
To do so just enter '**.combat**'
        ''')

# combat against the computer or another discord user
@bot.command(name='combat')
async def combat(ctx):
    player = dndbot.Character()
    if player.check_char_exists(ctx.author.id) == False:
        await ctx.send(f'''
Before you can enter combat you must create a character.
Enter '**.create**' to start creating a character.
        ''')
        return

    player.load_char_info(ctx.author.id)
    await ctx.send(f'''
**{ctx.author.name}'s** character **{player.name}'s** attributes are:
Strength: **{player.strength}**
Dexterity: **{player.dexterity}**
Constitution: **{player.constitution}**
Intelligence: **{player.intelligence}**
Wisdom: **{player.wisdom}**
Charisma: **{player.charisma}**
Enter '**1**' to play against the **computer**
Enter '**2**' to play against a **friend**
        ''')

    try:
        play_versus = await bot.wait_for('message',
            check=lambda message: message.author == ctx.author,
            timeout = 20)
        if play_versus.content.lower() == '1':
            await ctx.send('play vs comp placeholder message')
        elif play_versus.content.lower() == '2':
            await ctx.send('play vs friend placeholder message')
            await combat_PvP(ctx, player)
        else:
            await ctx.send('you must enter 1 or 2 placeholder message')
    except asyncio.TimeoutError:
        await ctx.send('Sorry, you took too long to respond')

# Player vs Player combat
async def combat_PvP(ctx, player_one):
    await ctx.send(f'''
Enter '**1**' to fight against **{ctx.author.name}'s**
 **{player_one.char_class}** **{player_one.char_race}**
    ''')
    try:
        opponent = await bot.wait_for('message',
            check=lambda message: message.author != ctx.author,
            timeout = 20)
        if opponent.content.lower() == '1':
            player_two = dndbot.Character()
            if player_two.check_char_exists(ctx.author.id) == False:
                await ctx.send(f'''
Before you can enter combat you must create a character.
Enter '**.create**' to start creating a character.
        ''')
            else:
                player_two.load_char_info(opponent.author.id)
                await ctx.send(f'''
**{player_two.name}** challenges **{player_one.name}** to combat!
        ''')
    except asyncio.TimeoutError:
        await ctx.send(f'''
Sorry, **{player_one.name}** is too scary, 
no one wanted to fight them.
    ''')




# Player vs NPC combat
async def combat_PvNPC(ctx):
    pass


bot.run(dndbot_token.token)

