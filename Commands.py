"""

This File contains the list of Commands, please look at the example commands or (tbw) documentation,

"""

import CommandClass
import EventHandlerClass
#or use EasyCommand
import EasyCommand

def testCommandFunction(args):
    args.pop(0)
    print('test complete')
    return

testCommand = EasyCommand.createCommand('/test', testCommandFunction, False, '-test', '-t', '/t')

# attach command
Commands = [testCommand]