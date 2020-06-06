import CommandHandler
import Commands

#entry point
def main():
    mainCommandHandler = CommandHandler.CommandHandler()
    mainCommandHandler.hookCommands(Commands.Commands)
    
    #loop
    while True:
        mainCommandHandler.postCommand(input(">: "))


if __name__ == "__main__":
    main()