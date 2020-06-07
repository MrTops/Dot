"""

This File contains the list of Commands, please look at the example commands or (tbw) documentation,

"""

import CommandClass
import EventHandlerClass

# make a function
def pingCommandFiredFunction(args):
    print("pong ;)")
    for thing in args:
        print(thing,end='')
    print()
    return

# make a event, name must be 'fired'
pingCommandFiredEvent = EventHandlerClass.EventObject('fired', pingCommandFiredFunction)

# make a event handler
pingCommandEventHandler = EventHandlerClass.EventHandler(pingCommandFiredEvent)

# make a command
pingCommand = CommandClass.Command('/ping', pingCommandEventHandler)

# attach command
Commands = [pingCommand]