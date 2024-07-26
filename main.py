import bot.actions as actions
import bot.helpers as helpers


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    command_handlers = {
        "hello": lambda args: actions.hello(),
        "add": lambda args: actions.add_contact(args, contacts),
        "change": lambda args: actions.change_contact(args, contacts),
        "phone": lambda args: actions.show_phone(args, contacts),
        "all": lambda args: actions.show_all(contacts),
        "exit": lambda args: actions.exit_bot(),
        "close": lambda args: actions.exit_bot(),
    }

    while True:
        user_input = input("Enter a command: ")
        command, args = helpers.parse_input(user_input)

        handler = command_handlers.get(command, lambda args: helpers.invalid_command())
        result = handler(args)
        if result:
            print(result)

if __name__ == "__main__":
    main()