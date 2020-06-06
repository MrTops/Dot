class CommandHandler(object):
    """
    
    This class handles IO for commands

    """

    def __init__(self):
        #init method
        self.hookedCommands = {}

    def hookCommands(self, commandList):
        #hook commands
        for command in commandList:
            self.hookedCommands[command.callSign] = command

    def postCommand(self, INPUT):
        parsed_INPUT = INPUT.split(' ')
        try:
            return self.hookedCommands[parsed_INPUT[0]].fire(parsed_INPUT)
        except Exception:
            return None