# HW_04.py

import colorama


def print_greeting() -> str:
    """
    Print a greeting and display a start menu for the user to continue
    or exit.
    :return: A string with instructions.
    """
    return (f'Welcome to the assistant bot!\nEnter '
            f'{colorama.Fore.GREEN}hello{colorama.Style.RESET_ALL} '
            f'to display the command menu or '
            f'{colorama.Fore.GREEN}exit{colorama.Style.RESET_ALL} '
            f'to exit.')


def print_instructions() -> str:
    """
    Display the main menu for the user to interact with the bot.
    :return: A string with instructions.
    """
    return (f'How can I help you?\nYour options:\n• '
            f'{colorama.Fore.GREEN}add <name> <phone>'
            f'{colorama.Style.RESET_ALL} to add a unique contact;\n• '
            f'{colorama.Fore.GREEN}edit <name> <phone>'
            f'{colorama.Style.RESET_ALL} to edit a phone by name;\n• '
            f'{colorama.Fore.GREEN}find <name>'
            f'{colorama.Style.RESET_ALL} to display a phone by name;\n• '
            f'{colorama.Fore.GREEN}find'
            f'{colorama.Style.RESET_ALL} to display all contacts;\n• '
            f'{colorama.Fore.GREEN}exit'
            f'{colorama.Style.RESET_ALL} to exit the bot.')


def parse_input(user_input) -> tuple:
    """
    Split the user input into separate values to be passed as a command
    and user data.
    :param user_input: User-entered data.
    :return: A tuple with processed values (command and list of user
    data).
    """
    command, *args = user_input.split()
    command = command.strip().casefold()
    return command, args


def add_contact(contacts, args) -> str:
    """
    Check the uniqueness of a contact and add it to the dictionary
    available during the program execution.
    :param contacts: Dictionary with contacts.
    :param args: A list of used data (name and phone).
    :return: A resulting message.
    """
    name, phone = args
    if name in contacts:
        return (f'The name already exists: '
                f'{colorama.Fore.BLUE}{name}{colorama.Style.RESET_ALL}. '
                f'Choose another one.')
    contacts[name] = phone
    return (f'The contact added: '
            f'{colorama.Fore.BLUE}{name}{colorama.Style.RESET_ALL}.')


def edit_contact(contacts, args) -> str:
    """
    Check the presence of a contact and edit it in the dictionary
    available during the program execution.
    :param contacts: Dictionary with contacts.
    :param args: A list of used data (name and phone).
    :return: A resulting message.
    """
    name, phone = args
    if name not in contacts:
        return (f'The name doesn\'t exist: '
                f'{colorama.Fore.BLUE}{name}{colorama.Style.RESET_ALL}. '
                f'You can add it.')
    contacts[name] = phone
    return (f'The contact edited: '
            f'{colorama.Fore.BLUE}{name}{colorama.Style.RESET_ALL}.')


def print_contacts(contacts, args) -> str:
    """
    Find the phone by name or all contacts stored in the dictionary.
    :param contacts: Dictionary with contacts.
    :param args: A list of used data (name and phone)
    :return: A single phone or all contacts, or a warning message.
    """
    contact_list = []
    if args:
        name_query = args[0]
        for name, phone in contacts.items():
            if name_query == name:
                return phone
        return 'No contact found.'
    else:
        for name, phone in contacts.items():
            contact_list.append(f'{name}: {phone}')
    contact_list.sort()
    return '\n'.join(contact_list) if contact_list else 'No contacts found.'


def main() -> None:
    """
    Validate the user data, print greeting and farewell messages,
    process the user choices, and print requested data or an error
    message.
    :return: None.
    """
    print(print_greeting())
    contacts = {}

    while True:
        try:
            user_input = input('Enter a command: ')
            if not user_input:
                continue
            command, args = parse_input(user_input)
            if command in ['close', 'exit']:
                print("Goodbye!")
                break
            elif command == 'hello':
                print(print_instructions())
            elif command.startswith('add'):
                print(add_contact(contacts, args))
            elif command.startswith('edit'):
                print(edit_contact(contacts, args))
            elif command.startswith('find'):
                print(print_contacts(contacts, args))
            else:
                print(f'Invalid command: '
                      f'{colorama.Fore.RED}{command}{colorama.Style.RESET_ALL}. '
                      f'If you want to continue, enter the correct one or '
                      f'{colorama.Fore.GREEN}exit{colorama.Style.RESET_ALL} '
                      f'to exit.')
        except ValueError:
            print(f'Invalid command format. See the menu for reference.')
            continue


if __name__ == "__main__":
    main()
