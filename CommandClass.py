class Command(object):
    """
    The command class describes a command and it's attributes!
    """
    def __init__(self, callSign, eventHandler):
        self.callSign = callSign
        self.eventHandler = eventHandler

    def fire(self, args):
        return self.eventHandler.callEvent("fired", args)