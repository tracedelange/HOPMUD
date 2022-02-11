"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter


class Character(DefaultCharacter):
    

    def at_object_creation(self):
        "This is called when object is first created, only."   

        name = 'Unnamed'

        self.db.name = name
        self.db.strength = 5
        self.db.agility = 4
        self.db.magic = 2
        self.db.health = 100
    
    def get_character(self):
        """
        Simple access method to return ability
        scores as a tuple (str,agi,mag)
        """
        return self.db.strength, self.db.agility, self.db.magic, self.db.health, self.db.name



    pass
