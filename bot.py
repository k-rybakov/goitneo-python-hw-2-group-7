def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter name and phone please."
        except IndexError:
            return 'Enter name please'
  
    return inner

@input_error
def parse_input(user_input):
    user_input = '' if None else user_input 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_phone(args, contacts):
    return contacts.get(args[0], "Contact not found")

@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name):
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found"

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
                print(add_contact(args, contacts))
        elif command == "change":
                print(change_contact(args, contacts))
        elif command == "phone":
                print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()