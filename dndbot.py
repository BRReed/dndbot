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

    def __init__(self, default=10):
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
            'Barbarian'
        ]
    
    def show_attributes(self):
        print(self.strength)
        print(self.dexterity)
        print(self.constitution)
        print(self.intelligence)
        print(self.wisdom)
        print(self.charisma)
        print(self.armorclass)

    def set_attribute(self, attribute, value):
        if attribute == 'Strength':
            self.strength = value
            return self.strength
        elif attribute == 'Dexterity':
            self.dexterity = value
            return self.dexterity
        elif attribute == 'Constitution':
            self.constitution = value
            return self.constitution
        elif attribute == 'Intelligence':
            self.intelligence = value
            return self.intelligence
        elif attribute == 'Wisdom':
            self.wisdom = value
            return self.wisdom
        elif attribute == 'Charisma':
            self.charisma = value
            return self.charisma
        else:
            print('set attribute in character class whoops')
        
    def set_char_class(self, char_class):
        self.char_class = char_class
        print(f'youre a {self.char_class} harry')
        

        
        
    



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
            
    def set_char_class(self):
        print(self.classes)
        print('Choose a class from the classes above')
        no_class = True
        while no_class:
            try:
                get_char_class = input('>')
                if get_char_class in self.classes:
                    no_class = False
                    Character.set_char_class(self, get_char_class)
                    
                else:
                    print('Sorry, that class isn\'t available '
                          'please retype:')
            except ValueError:
                print('error getting class, please try again')

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



class NonPlayer(Character):

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
p = Player()
p.set_attributes()
p.print_attributes()
p.set_char_class()
'''
Set Up
'''

'''
Main Loop
'''