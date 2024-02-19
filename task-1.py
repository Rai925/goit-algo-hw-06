from typing import List
from collections import UserDict

class Field:
    def __init__(self, value: str):
        if not value:
            raise ValueError
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        if not value.strip():
            raise ValueError
        super().__init__(value)

class Phone(Field):
    def __init__(self, value: str):
        if not value.isdigit() or len(value) != 10:
            raise ValueError
        super().__init__(value)

class Record:
    def __init__(self, name: Name):
        self.name = Name(name)
        self.phones: List[Phone] = []

    def add_phone(self, phone_number: str):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number: str):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone_number: str, new_phone_number: str):
        if not new_phone_number.isdigit() or len(new_phone_number) != 10:
            raise ValueError
        phone_exists = False
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone_exists = True
                phone.value = new_phone_number
                break
        if not phone_exists:
            raise ValueError

    def find_phone(self, phone_number: str) -> Phone:
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        phone_numbers = '; '.join(phone.value for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_numbers}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]
