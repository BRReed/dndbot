import random
import json


'''
Objects
'''
def roll_die(dice, sides):
    random.seed()
    total = 0
    for _ in range(0, dice):
        total += random.randint(1, sides + 1)

    return total

def combat_initiative(player_one, player_two):
    try:
        player_one_initiative = roll_die(1, 20)
        player_two_initiative = roll_die(1, 20)
        player_one_initiative != player_two_initiative
    finally:
        if player_one_initiative > player_two_initiative:
            p1 = True
            return p1, player_one_initiative, player_two_initiative
        elif player_one_initiative < player_two_initiative:
            p1 = False
            return p1, player_one_initiative, player_two_initiative
        else:
            print(f'problem in combat_initiative '+
                  f'p1 = {player_one}; p2 = {player_two} '+
                  f'p1 roll = {player_one_initiative}; '+
                  f'p2 roll = {player_two_initiative}')



class Character():

    def __init__(self, default=0):
        self.strength_mod = default
        self.dexterity_mod = default
        self.constitution_mod = default
        self.intelligence_mod = default
        self.wisdom_mod = default
        self.charisma_mod = default
        self.strength = default
        self.dexterity = default
        self.constitution = default
        self.intelligence = default
        self.wisdom = default
        self.charisma = default
        self.armorclass = default
        self.attribute_scores = [15, 14, 13, 12, 10, 8]
        self.attributes = [
            'Strength', 
            'Dexterity', 
            'Constitution', 
            'Intelligence', 
            'Wisdom', 
            'Charisma'
        ]
        self.classes = [
            'Barbarian',
            'Fighter',
            'Monk',
            'Paladin',
            'Rogue'
        ]
        self.resistances = [

        ]
        self.advantages = [

        ]
        self.proficiencies = [

        ]
        # Character.results[0] == wins
        # Character.results[1] == losses
        self.results = [0, 0]
    
    def show_attributes(self):
        print(self.strength)
        print(self.dexterity)
        print(self.constitution)
        print(self.intelligence)
        print(self.wisdom)
        print(self.charisma)
        print(self.armorclass)

    def show_modifiers(self):
        print(self.strength_mod)
        print(self.dexterity_mod)
        print(self.constitution_mod)
        print(self.intelligence_mod)
        print(self.wisdom_mod)
        print(self.charisma_mod)

    # discord bot prints characters proficiencies
    def show_proficiencies(self):
        self.print_proficiencies = (f'')
        for p in self.proficiencies:
            self.print_proficiencies += f'\n**{p}**'

    # takes a characters attributes and adjusts that attributes modifier
    ## takes attribute, makes value = attribute, takes value assigns
    ## modifier based on that, takes modifier and assigns attribute_mod
    def set_attribute_modifier(self):
        for attribute in self.attributes:
            if attribute == 'Strength':
                value = self.strength
            elif attribute == 'Dexterity':
                value = self.dexterity
            elif attribute == 'Constitution':
                value = self.constitution
            elif attribute == 'Intelligence':
                value = self.intelligence
            elif attribute == 'Wisdom':
                value = self.wisdom
            elif attribute == 'Charisma':
                value = self.charisma
            else:
                print(f'problem in set value '+
                    f'attr = {attribute}; val = {value}')
            if value == 1:
                modifier = -5
            elif value == 2 or value == 3:
                modifier = -4
            elif value == 4 or value == 5:
                modifier = -3
            elif value == 6 or value == 7:
                modifier = -2
            elif value == 8 or value == 9:
                modifier = -1
            elif value == 10 or value == 11:
                modifier = 0
            elif value == 12 or value == 13:
                modifier = 1
            elif value == 14 or value == 15:
                modifier = 2
            elif value == 16 or value == 17:
                modifier = 3
            elif value == 18 or value == 19:
                modifier = 4
            elif value == 20 or value == 21:
                modifier = 5
            elif value == 22 or value == 23:
                modifier = 6
            elif value == 24 or value == 25:
                modifier = 7
            elif value == 26 or value == 27:
                modifier = 8
            elif value == 28 or value == 29:
                modifier = 9
            elif value == 30:
                modifier = 10
            else:
                print(f'problem in set modifier if/else statement '+
                    f'attr = {attribute}; mod = {modifier}; val = {value}')
            if attribute == 'Strength':
                self.strength_mod = modifier
            elif attribute == 'Dexterity':
                self.dexterity_mod = modifier
            elif attribute == 'Constitution':
                self.constitution_mod = modifier
            elif attribute == 'Intelligence':
                self.intelligence_mod = modifier
            elif attribute == 'Wisdom':
                self.wisdom_mod = modifier
            elif attribute == 'Charisma':
                self.charisma_mod = modifier
            else:
                print(f'problem in set set attritube_mod = modifier '+
                    f'attr = {attribute}; mod = {modifier}; val = {value}')
        self.armorclass = (10 + self.dexterity_mod)


    # takes a characters class, changes character attributes to match class
    def set_char_class(self, char_class):
        self.char_class = char_class
        if self.char_class == 'Barbarian':
            self.constitution = 15
            self.strength = 14
            self.dexterity = 13
            self.charisma = 12
            self.wisdom = 10
            self.intelligence = 8
        elif self.char_class == 'Paladin':
            self.strength = 15
            self.constitution = 14
            self.charisma = 13
            self.dexterity = 12
            self.wisdom = 10
            self.intelligence = 8
        elif self.char_class == 'Fighter':
            self.strength = 15
            self.constitution = 14
            self.dexterity = 12
            self.charisma = 13
            self.wisdom = 10
            self.intelligence = 8
        elif self.char_class == 'Monk':
            self.dexterity = 15
            self.wisdom = 14
            self.constitution = 13
            self.charisma = 12
            self.intelligence = 10
            self.strength = 8
        elif self.char_class == 'Rogue':
            self.dexterity = 15
            self.charisma = 14
            self.strength = 13
            self.constitution = 12
            self.wisdom = 10
            self.intelligence = 8
        else:
            print('Error in function set_char_class in class Character')
            print(f'the passed value for char_class is: {char_class}')
    
    # takes a characters race, changes character attributes based on race
    def set_char_race(self, char_race):
        self.char_race = char_race
        if self.char_race == 'Dwarf':
            self.constitution += 2
            self.resistances.append('Poison')
            self.advantages.append('Poison')
            self.proficiencies.append('Battleaxe', 'Handaxe',
                                   'Light Hammer', 'Warhammer')
        elif self.char_race == 'Elf':
            self.dexterity += 2
            self.resistances.append('Sleep')
            self.advantages.append('Charmed')
            self.proficiencies += ('**')
        elif self.char_race == 'Human':
            self.strength += 1
            self.constitution += 1
            self.dexterity += 1
            self.charisma += 1
            self.wisdom += 1
            self.intelligence += 1

    # takes a weapon and gives it to character, changes attributes based
    # on character proficiencies of applicable
    def set_char_weapon(self, weapon):
        self.weapon = weapon
        if self.weapon == 'Battleaxe':
            self.weapon_attack = 8
            self.weapon_attack_type = 'Slashing'
        elif self.weapon == 'Longsword':
            self.weapon_attack = 8
            self.weapon_attack_type = 'Slashing'
        elif self.weapon == 'Warhammer':
            self.weapon_attack = 8
            self.weapon_attack_type = 'Bludgeoning'
        else:
            pass
        if self.weapon in self.proficiencies:
            self.weapon_attack += 2
        else:
            pass

    # takes a string and checks for illegal characters
    # returns False if string contains illegal characters, True if it doesn't
    def set_char_name(self, name):
        self.name = name
        lowered_name = self.name.lower()
        if len(self.name) > 30:
            return False
        list_name = [c for c in lowered_name]
        allowed_characters = ('a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ')
        for c in list_name:
            if c not in allowed_characters:
                self.name = ''
                return False
            else: 
                continue
        self.name = self.name.upper()
        return True

    # takes current instance and saves to json file
    def save_char_info(self, userID):
        with open('dndbot_saves.json') as f:
            data = json.load(f)
        data[f'{userID}'] = self.instance_as_dictionary()
        with open('dndbot_saves.json', 'w') as f:
            json.dump(data, f)


    # Takes current instance of character and returns as dictionary
    def instance_as_dictionary(self):
        dict_of_inst = {
            'strength_mod': self.strength_mod, 'strength': self.strength,
            'dexterity_mod': self.dexterity_mod, 'dexterity': self.dexterity,
            'constitution_mod': self.constitution_mod,
            'constitution': self.constitution, 
            'intelligence_mod': self.intelligence_mod,
            'intelligence': self.intelligence,
            'wisdom_mod': self.wisdom_mod, 'wisdom': self.wisdom, 
            'charisma_mod': self.charisma_mod, 'charisma': self.charisma,
            'armorclass': self.armorclass, 'resistances': self.resistances,
            'advantages': self.advantages, 'proficiencies': self.proficiencies,
            'results': self.results, 'char_class': self.char_class,
            'char_race': self.char_race, 'weapon': self.weapon,
            'weapon_attack': self.weapon_attack,
            'weapon_attack_type': self.weapon_attack_type, 'name': self.name
        }
        return dict_of_inst

    # takes a dictionary of a character and modifies current instance 
    # to dictionary specifications
    def dictionary_as_instance(self, char_dict):
        self.strength_mod = char_dict['strength_mod']
        self.strength = char_dict['strength']
        self.dexterity_mod = char_dict['dexterity_mod']
        self.dexterity = char_dict['dexterity']
        self.constitution_mod = char_dict['constitution_mod']
        self.constitution = char_dict['constitution']
        self.intelligence_mod = char_dict['intelligence_mod']
        self.intelligence = char_dict['intelligence']
        self.wisdom_mod = char_dict['wisdom_mod']
        self.wisdom = char_dict['wisdom']
        self.charisma_mod = char_dict['charisma_mod']
        self.charisma = char_dict['charisma']
        self.armorclass = char_dict['armorclass']
        self.resistances = char_dict['resistances']
        self.advantages = char_dict['advantages']
        self.proficiencies = char_dict['proficiencies']
        self.results = char_dict['results']
        self.char_class = char_dict['char_class']
        self.char_race = char_dict['char_race']
        self.weapon = char_dict['weapon']
        self.weapon_attack = char_dict['weapon_attack']
        self.weapon_attack_type = char_dict['weapon_attack_type']
        self.name = char_dict['name']


    # access json file and loads character instance
    def load_char_info(self, userID):
        with open('dndbot_saves.json') as f:
            data = json.load(f)
        character_dictionary = data[f'{userID}']
        return self.dictionary_as_instance(character_dictionary)

    # checks if the user's discord ID exists as a key
    def check_char_exists(self, userID):
        with open('dndbot_saves.json') as f:
            data = json.load(f)
        if str(userID) in data:
            return True
        else:
            return False




class Player(Character):

    def __init__(self):
        Character.__init__(self)

    def print_attributes(self):
        print(self.strength)
        print(self.dexterity)
        print(self.constitution)
        print(self.intelligence)
        print(self.wisdom)
        print(self.charisma)
        print(self.armorclass)

    def print_modifiers(self):
        print(self.strength_mod)
        print(self.dexterity_mod)
        print(self.constitution_mod)
        print(self.intelligence_mod)
        print(self.wisdom_mod)
        print(self.charisma_mod)

    def set_attributes(self):
        while (len(self.attribute_scores) > 0):
            for attribute_name in self.attributes:
                print(self.attribute_scores)
                print('From the scores above ' +
                      'choose which you would like to set for ' +
                      f'{attribute_name}')
                not_valid = True
                while not_valid:
                    try:
                        get_value = int(input('>'))
                        get_index = self.attribute_scores.index(get_value)
                        not_valid = False
                    except ValueError:
                        print('Enter a value on the list')
                        print(self.attribute_scores)
                        not_valid = True
                Character.set_attribute(self, attribute_name, get_value)
                self.attribute_scores.pop(get_index)

    def set_hit_points(self):
        pass
    
    def set_proficiencies(self):
        pass

    def set_equipment(self):
        pass

    def set_abilities(self):
        pass

    def set_attacks(self):
        pass

    def set_spells(self):
        pass



class AutoSelectPlayer(Character):

    def __init__(self):
        Character.__init__(self)

    def set_attributes(self):

        for attribute_name in self.attributes:
            value = random.choice(self.attribute_scores)
            index = self.attribute_scores.index(value)
            Character.set_attribute(self, attribute_name, value)
            self.attribute_scores.pop(index)
    
    def print_attributes(self):
        print(self.strength)
        print(self.dexterity)
        print(self.constitution)
        print(self.intelligence)
        print(self.wisdom)
        print(self.charisma)
        print(self.armorclass)

    def set_npc_class(self):
        pass


class Item():
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

class Weapon(Item):
    def __init__(self, weight, name, damage):
        Item.__init__(self, weight, name)
        self.damage = damage

class Consumable(Item):
    def __init__(self, weight, name, uses):
        Item.__init__(self, weight, name)
        self.uses = uses

#np = Character()
#print(np.set_char_name('Bjord Elfenstien*'))
'''
Set Up
'''

'''
Main Loop
'''