from .helpers import input_error
from .record import Record


@input_error
def add_contact(args, book):
    if len(args) != 2:
        raise ValueError

    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."


@input_error
def change_contact(args, book):
    if len(args) != 3:
        raise ValueError
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, book):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    record = book.find(name)
    if record:
        return str(record)
    else:
        raise KeyError


@input_error
def show_all(book):
    return "\n".join(str(record) for record in book.values())


@input_error
def add_birthday(args, book):
    if len(args) != 2:
        raise ValueError
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError


@input_error
def show_upcoming_birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join(f"{item['name']}: {item['congratulation_date']}" for item in upcoming_birthdays)
    else:
        return "No upcoming birthdays."


def hello():
    return "How can I help you?"


def exit_bot():
    print("Good bye!")
    exit()
