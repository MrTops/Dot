class Command(object):
    """
    The command class describes a command and it's attributes!
    """
    def __init__(self, callSign, eventHandler, useStrict=True, *alias):
        self.callSign = callSign
        self.eventHandler = eventHandler
        self.alias = alias
        self.useStrict = useStrict

    def fire(self, args):
        return self.eventHandler.callEvent("fired", args)