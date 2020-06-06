"""

This File contains the list of Commands, please look at the example commands or (tbw) documentation,

"""

import CommandClass
import EventHandlerClass


def pingFiredEventFunction(*args):
    print("  pong")

pingFiredEvent = EventHandlerClass.EventObject('fired', pingFiredEventFunction)
pingEventHandler = EventHandlerClass.EventHandler(pingFiredEvent)
pingCommand = CommandClass.Command("/ping", pingEventHandler)

Commands = [
    pingCommand
]