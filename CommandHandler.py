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
            self.hookedCommands[command.callSign.lower()] = command
            for alia in command.alias[0]:
                self.hookedCommands[alia.lower()] = command

    def postCommand(self, INPUT):
        parsed_INPUT = INPUT.split(' ')
        try:
            commandFound = self.hookedCommands[parsed_INPUT[0].lower()]
            if commandFound.useStrict:
                if parsed_INPUT[0] == commandFound.callSign:
                    return commandFound.fire(parsed_INPUT) 
                elif parsed_INPUT[0] in commandFound.alias[0]:
                    return commandFound.fire(parsed_INPUT)
            elif not commandFound.useStrict:
                if parsed_INPUT[0].lower() == commandFound.callSign.lower():
                    return commandFound.fire(parsed_INPUT) 
                else:
                    runCommand = False
                    for alia in commandFound.alias[0]:
                        if parsed_INPUT[0].lower() == alia.lower():
                            runCommand = True
                            break

                    if runCommand:
                        return commandFound.fire(parsed_INPUT)

            return None
        except Exception:
            return None