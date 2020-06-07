"""

This File contains the list of Commands, please look at the example commands or (tbw) documentation,

"""

import CommandClass
import EventHandlerClass
#or use EasyCommand
import EasyCommand

## Easy Command
# make a function
def oofCommandFiredFunction(args):
    args.pop(0)
    print("oof")
    return

# make a command
oofCommand = EasyCommand.createCommand('/oof', oofCommandFiredFunction)

# (below) attach command to list

## Long Way
# make a function
def pingCommandFiredFunction(args):
    print("pong ;)")
    # pop first
    args.pop(0)
    for thing in args:
        print(thing,end=' ')
    print()
    return

# make a event, name must be 'fired'
pingCommandFiredEvent = EventHandlerClass.EventObject('fired', pingCommandFiredFunction)

# make a event handler
pingCommandEventHandler = EventHandlerClass.EventHandler(pingCommandFiredEvent)

# make a command
pingCommand = CommandClass.Command('/ping', pingCommandEventHandler)

# attach command
Commands = [pingCommand, oofCommand]