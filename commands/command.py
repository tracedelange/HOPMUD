"""
Commands

Commands describe the input the account can do to the game.

"""

from unicodedata import name
from evennia.commands.command import Command as BaseCommand
import random

# from evennia import default_cmds


class Command(BaseCommand):
    """
    Inherit from this if you want to create your own command styles
    from scratch.  Note that Evennia's default commands inherits from
    MuxCommand instead.

    Note that the class's `__doc__` string (this text) is
    used by Evennia to create the automatic help entry for
    the command, so make sure to document consistently here.

    Each Command implements the following methods, called
    in this order (only func() is actually required):
        - at_pre_cmd(): If this returns anything truthy, execution is aborted.
        - parse(): Should perform any extra parsing needed on self.args
            and store the result on self.
        - func(): Performs the actual work.
        - at_post_cmd(): Extra actions, often things done after
            every command, like prompts.

    """

    pass


class CmdSetPower(Command):
    """
    set the power of a character

    Usage: 
      +setpower <1-10>

    This sets the power of the current character. This can only be 
    used during character generation.    
    """
    
    key = "+setpower"
    help_category = "mush"

    def func(self):
        "This performs the actual command"
        errmsg = "You must supply a number between 1 and 10."
        if not self.args:
            self.caller.msg(errmsg)      
            return
        try:
            power = int(self.args)  
        except ValueError:
            self.caller.msg(errmsg)
            return
        if not (1 <= power <= 10):
            self.caller.msg(errmsg)
            return
        # at this point the argument is tested as valid. Let's set it.
        self.caller.db.power = power
        self.caller.msg("Your Power was set to %i." % power)


class CmdCharacter(Command):
    """
    List Character Information

    Usage:
        character

    Displays all relevant information about your character
    """
    key = "character"
    aliases = ["char"]
    lock = "cmd:all()"
    help_category = "General"

    def func(self):

        str, agi, mag, health, name = self.caller.get_character()

        string = """
        Stats for %s
        ------------------
        HP: %s\n
        STR: %s\n
        AGI: %s\n
        MAG: %s
        """ % (name, health, str, agi, mag)

        self.caller.msg(string)