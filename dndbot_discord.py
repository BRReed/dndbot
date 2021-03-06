import discord
import asyncio
from discord.ext import commands
import dndbot
import dndbot_token
import dndbot_roll


bot = commands.Bot(command_prefix = '.')


@bot.event
async def on_ready():
    '''
    Prints to console when bot is initialized
    '''
    print('Bot is ready.')
    activity = discord.Game(name=".commands")
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.command(name='shutdown')
async def shutdown(message):
    '''
    shutdown from authorized user
    action: shuts bot down
    '''
    if str(message.author.id) == '275827627502075905':
        print('bot closed')
        await bot.close()
    else:
        print('unauthorized user ' + str(message.author.id) +
              ' is trying to close the bot')
              

@bot.command(name='commands')
async def user_commands(ctx):
    '''
    Prints available commands to channel
    '''
    await ctx.send(
        """
**.dicegame** - Whoever rolls higher wins
**.combat** - Play a game of DND combat (caution - boring in current state)
**.commands** - Get a list of commands
**.create** - Make a DND character 
**.wins** - Show the wins and losses of your character
        """
    )


@bot.command(name='dicegame')
async def dice_game(ctx):
    '''
    Plays one round of higher/lower with 2 6 sided dice 
    Initiator can choose to play against either comp or another user
    '''
    
    await ctx.channel.send("type '1' to play against computer,"+
                           "'2' to wait for another player")
    choice = await bot.wait_for('message',
            check=lambda message: message.author == ctx.author)
    if choice.content.lower() == '1':
        player = dndbot.roll_die(2, 6)
        computer = dndbot.roll_die(2, 6)
        if computer > player:
            result = "Computer Wins!"
        elif computer < player:
            result = "Player Wins!"
        else:
            result = "Tie!"
        await ctx.channel.send("You want to play with the computer\n"+
                              f"you rolled {player}\n"+
                              f"computer rolled {computer}\n"+
                              f"{result}")
    elif choice.content.lower() == '2':
        await ctx.channel.send(
            "You want to play against another player\n"+
            "If you want to play against"+
           f" {ctx.author} type '1'")
        try:
            player2 = await bot.wait_for('message',
                check=lambda message: message.author != ctx.author,
                timeout = 20)
            if player2.content.lower() == '1':
                player_dice_total = dndbot.roll_die(2, 6)
                player2_dice_total = dndbot.roll_die(2, 6)
                if player_dice_total > player2_dice_total:
                    result = f'{ctx.author} Wins!'
                elif player_dice_total < player2_dice_total:
                    result = f'{player2.author} Wins!'
                else:
                    result = 'Tie!'
                await ctx.channel.send(
                    f"{ctx.author} vs {player2.author}\n"+
                    f"{ctx.author}'s total:"+
                    f" {player_dice_total}\n"+
                    f"{player2.author}'s total:"+
                    f" {player2_dice_total}\n"+
                    f"{result}")


        except asyncio.TimeoutError:
            await ctx.channel.send('''
Sorry, no one wants to play with you!
''')

@bot.command(name='wins')
async def character_wins(ctx):
    p = dndbot.Character()
    if p.check_char_exists(ctx.author.id) == False:
        await ctx.send(f'''
Before you can check your win/loss ratio you must create a character.
Enter '**.create**' to start creating a character.
        ''')
        return
    elif p.check_char_exists(ctx.author.id) == True:
        p.load_char_info(ctx.author.id)
        await ctx.send(f'''
**{p.name}**'s wins: **{p.results[0]}**
**{p.name}**'s losses: **{p.results[1]}**
        ''')
        return

@bot.command(name='create')
async def create_character(ctx):
    '''
    Create a character for dnd combat based on user input
    '''
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
    player_create.show_proficiencies()
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

@bot.command(name='roll')
async def roll(ctx):
    '''
    Rolls a 1000 sided die
    '''
    roll = dndbot.roll_die(1, 1000)
    result = dndbot_roll(roll)
    await ctx.channel.send(result)


@bot.command(name='combat')
async def combat(ctx):
    """
    Play a round of dnd combat against computer or another user
    """
    player = dndbot.Character()
    if player.check_char_exists(ctx.author.id) == False:
        await ctx.send('''
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
    player.hit_points = (player.hit_die + player.constitution_mod)
    print(player.hit_points)
    try:
        play_versus = await bot.wait_for('message',
            check=lambda message: message.author == ctx.author,
            timeout = 20)
        if play_versus.content.lower() == '1':
            await combat_PvNPC(ctx, player)
        elif play_versus.content.lower() == '2':
            await combat_PvP(ctx, player)
    except asyncio.TimeoutError:
        await ctx.send('Sorry, you took too long to respond')


async def combat_PvP(ctx, player_one):
    """
    Combat vs another user
    """
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
**{player_one.name}** is too scary, 
no one wanted to fight them.
    ''')
    player_two.hit_points = (player_two.hit_die + player_two.constitution_mod)
    init, player_one_init, player_two_init = dndbot.combat_init(ctx.author.id, 
                                                            opponent.author.id)
    if init is True:
        turn_order = [player_one, player_two]
    elif init is False:
        turn_order = [player_two, player_one]
    await ctx.send(f'''
**{player_one.name}** initiative roll: **{player_one_init}**
**{player_two.name}** initiative roll: **{player_two_init}**
''')

    a_player = 0
    p_player = 1
    while True:
        await ctx.send(f'''
**{turn_order[a_player].name}** 
Enter '1' to attack **{turn_order[p_player].name}**
Enter '2' to run
''')

        player_action = await bot.wait_for('message',
        check=lambda message: message.author.id == turn_order[a_player].userID)
        if player_action.content.lower() == '1':
            attack_roll, damage_roll = dndbot.combat(turn_order[a_player], 
                                                     turn_order[p_player])
            if attack_roll >= turn_order[p_player].armorclass:
                await ctx.send(f"**{turn_order[a_player].name}** hit "+
                        f"**{turn_order[p_player].name}** for {damage_roll}",
                        f"{turn_order[p_player].name}'s HP is now "+
                        f"{turn_order[p_player].hit_points}")
            elif attack_roll < turn_order[p_player].armorclass:
                await ctx.send(f"**{turn_order[a_player].name}** swings and "+
                               f"misses **{turn_order[p_player].name}**")
            else:
                print('error in attack roll / armor class evaluation '+
                      'dndbot_discord'+
                      f'armor class: {turn_order[p_player].armorclass}'+
                      f'attack roll: {attack_roll}')
        if player_one.hit_points <= 0:
            await ctx.send(f'''
**{player_one.name}** has fallen in combat
**{player_two.name}** is victorious!
''')
            player_one.results[1] += 1
            player_two.results[0] += 1
            player_one.save_char_info(player_one.userID)
            player_two.save_char_info(player_two.userID)
            break
        elif player_two.hit_points <= 0:
            await ctx.send(f'''
**{player_two.name}** has fallen in combat
**{player_one.name}** is victorious!
''')
            player_one.results[0] += 1
            player_two.results[1] += 1
            player_one.save_char_info(player_one.userID)
            player_two.save_char_info(player_two.userID)
            break
        else:
            pass
        if a_player + 1 < len(turn_order):
            a_player += 1
        else:
            a_player = 0
        if p_player + 1 < len(turn_order):
            p_player += 1
        else:
            p_player = 0


async def combat_PvNPC(ctx, player_one):
    """
    Combat vs computer
    """
    npc = dndbot.Character()
    npc.comp_create_char()
    npc.set_attribute_modifier()
    npc.save_char_info('757334164914700379')
    print(npc.instance_as_dictionary('757334164914700379'))
    init, player_one_init, npc_init = (
        dndbot.combat_init(ctx.author.id, '757334164914700379')
    )
    if init is True:
        turn_order = [player_one, npc]
    elif init is False:
        turn_order = [npc, player_one]
    await ctx.send(f'''
**{player_one.name}** initiative roll: **{player_one_init}**
**{npc.name}** initiative roll: **{npc_init}**
''')
    a_player = 0
    p_player = 1
    while True:
        await ctx.send(f'''
**{turn_order[a_player].name}** 
Enter '1' to attack **{turn_order[p_player].name}**
Enter '2' to run
''')
        if turn_order[a_player].bot == True:
            await asyncio.sleep(5)
            attack_roll, damage_roll = dndbot.combat(turn_order[a_player], 
                                                     turn_order[p_player])
            await ctx.send(f'{attack_roll}, {damage_roll}')
        else:
            pass
        if turn_order[a_player].bot == False:
            player_action = await bot.wait_for(
                'message', check=lambda message: message.author.id == (
                turn_order[a_player].userID)
            )
            if player_action.content.lower() == '1':
                attack_roll, damage_roll = dndbot.combat(turn_order[a_player], 
                                                         turn_order[p_player])
        if attack_roll >= turn_order[p_player].armorclass:
            await ctx.send(f"**{turn_order[a_player].name}** hit "+
                           f"**{turn_order[p_player].name}** for {damage_roll}",
                           f"{turn_order[p_player].name}'s HP is now "+
                           f"{turn_order[p_player].hit_points}")
        elif attack_roll < turn_order[p_player].armorclass:
            await ctx.send(f'**{turn_order[a_player].name}** swings and '+
                           f'misses **{turn_order[p_player].name}**')
        else:
            print('error in attack roll / armor class evaluation '+
                  'dndbot_discord '+
                 f'armor class: {turn_order[p_player].armorclass} '+ 
                 f'attack roll: {attack_roll}')
        if player_one.hit_points <= 0:
            await ctx.send(f'''
**{player_one.name}** has fallen in combat
**{npc.name}** is victorious!
''')
            player_one.results[1] += 1
            player_one.save_char_info(player_one.userID)
            break
        elif npc.hit_points <= 0:
            await ctx.send(f'''
**{npc.name}** has fallen in combat
**{player_one.name}** is victorious!
''')
            player_one.results[0] += 1
            player_one.save_char_info(player_one.userID)
            break
        else:
            pass
        if a_player + 1 < len(turn_order):
            a_player += 1
        else:
            a_player = 0
        if p_player + 1 < len(turn_order):
            p_player += 1
        else:
            p_player = 0

bot.run(dndbot_token.token)
