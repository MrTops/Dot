"""

Offers an easy IO based way of creating a command

instead of:
function -> eventObject -> eventHandlerObject -> commandObject

do this:
function -> commandObject

"""

import CommandClass
import EventHandlerClass

def createCommand(name, function):
    eventObject = EventHandlerClass.EventObject('fired', function)
    eventHandlerObject = EventHandlerClass.EventHandler(eventObject)
    return CommandClass.Command(name, eventHandlerObject)