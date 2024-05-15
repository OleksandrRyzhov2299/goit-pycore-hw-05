def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "🟡 Give me name and phone please."
        except KeyError:
            return "🟡 Contact does not exist"
        except IndexError:
            return "🟡 Enter contact name"
        except:
            return "🔴 Some error is occured. We are working on a solution"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "✅ Contact added"


@input_error
def show_phone(args: list, contacts: dict) -> str:
    name = args[0]
    phone_number = contacts[name]
    return f"🏷️  {name}: 📱 {phone_number}"


@input_error
def change_contact(contact_for_change: list, contacts: dict) -> str:
    contact_name, contact_phone = contact_for_change
    for contact in contacts:
        if contact_name == contact:
            contacts[contact_name] = contact_phone
            return "✅ Contact updated"

    raise KeyError()


@input_error
def show_all(contacts: dict) -> str:
    if not contacts:
        return "📒 Contact book is empty"

    printed_contatcs = ""
    for key, value in contacts.items():
        printed_contatcs += f"📒: {key} 📱: {value}\n"
    return printed_contatcs


def main():
    # phone_book = {"Mango": "099-123-45-67"}
    phone_book = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *info = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(info, phone_book))
        elif command == "phone":
            print(show_phone(info, phone_book))
        elif command == "change":
            print(change_contact(info, phone_book))
        elif command == "all":
            print(show_all(phone_book))
        else:
            print("❌ Invalid command")


if __name__ == "__main__":
    main()
