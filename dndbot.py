import random

'''
Objects
'''
def roll_die(dice, sides):
    random.seed()
    total = 0
    for _ in range(0, dice):
        total += random.randint(1, sides + 1)

    return total


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
            'Rogue',

        ]
    
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

    
    # manually set attributes, possible use in the future currently not
    # implemented
    def set_attribute(self, attribute, value):
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
            print('problem in set_attribute modifier if/else statement')
        if attribute == 'Strength':
            self.strength = value
            self.strength_mod = modifier
            return self.strength, self.strength_mod
        elif attribute == 'Dexterity':
            self.dexterity = value
            self.dexterity_mod = modifier
            return self.dexterity, self.dexterity_mod
        elif attribute == 'Constitution':
            self.constitution = value
            self.constitution_mod = modifier
            return self.constitution, self.constitution_mod
        elif attribute == 'Intelligence':
            self.intelligence = value
            self.intelligence_mod = modifier
            return self.intelligence, self.intelligence_mod
        elif attribute == 'Wisdom':
            self.wisdom = value
            self.wisdom_mod = modifier
            return self.wisdom, self.wisdom_mod
        elif attribute == 'Charisma':
            self.charisma = value
            self.charisma_mod = modifier
            return self.charisma, self.charisma_mod
        else:
            print('set attribute in character class whoops')


    # takes a class, changes character attributes to match class    
    def set_char_class(self, char_class):
        if char_class == 'Barbarian':
            self.constitution == 15
            self.strength == 14
            self.dexterity == 13
            self.charisma == 12
            self.wisdom == 10
            self.intelligence == 8
        elif char_class == 'Paladin':
            self.strength == 15
            self.constitution == 14
            self.charisma == 13
            self.dexterity == 12
            self.wisdom == 10
            self.intelligence == 8
        elif char_class == 'Fighter':
            self.strength == 15
            self.constitution == 14
            self.dexterity == 12
            self.charisma == 13
            self.wisdom == 10
            self.intelligence == 8
        elif char_class == 'Monk':
            self.dexterity == 15
            self.wisdom == 14
            self.constitution == 13
            self.charisma == 12
            self.intelligence == 10
            self.strength == 8
        elif char_class == 'Rogue':
            self.dexterity == 15
            self.charisma == 14
            self.strength == 13
            self.constitution == 12
            self.wisdom == 10
            self.intelligence == 8
        else:
            print('Error in function set_char_class in class Character')
            print(f'the passed value for char_class is: {char_class}')
        



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

# np = NonPlayer()
# np.set_attributes()
# np.print_attributes()
# p = Player()
# p.set_attributes()
# p.print_attributes()
# p.set_char_class()
# p.print_attributes()
# p.print_modifiers()
'''
Set Up
'''

'''
Main Loop
'''