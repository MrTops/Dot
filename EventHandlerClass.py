class EventHandler(object):
    """
    This class describes a event IO system, this is custom and used cause I'm lazy
    """
    def __init__(self, *events):
        #init function
        #create var and hook it
        self.hookedEvents = {}
        for event in events:
            self.hookedEvents[event.getName()] = event.getFunction()
    
    def callEvent(self, eventName, args):
        #call event
        try:
            return self.hookedEvents[eventName](args)
        except Exception:
            return None

class EventObject(object):
    """
    This class describes a single event object which can be subscribed to an event handler
    """
    def __init__(self, name, function):
        #init function
        self.name = name
        self.function = function
        
    def getName(self):
        #get the objects name
        return self.name

    def getFunction(self):
        #get the objects function
        return self.function
    


            