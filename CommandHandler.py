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
            if command.useStrict:
                self.hookedCommands[command.callSign] = command
                if command.alias:
                    for alia in command.alias:
                        self.hookedCommands[alia] = command
            else:
                self.hookedCommands[command.callSign.lower()] = command
                if command.alias:
                    for alia in command.alias:
                        self.hookedCommands[alia.lower()] = command

    def postCommand(self, INPUT):
        parsed_INPUT = INPUT.split(' ')
        try:
            try:
                commandFound = self.hookedCommands[parsed_INPUT[0].lower()]
                return commandFound.fire(parsed_INPUT) 
            except Exception:
                commandFound = self.hookedCommands[parsed_INPUT[0]]
                return commandFound.fire(parsed_INPUT)
        except Exception:
            return None