from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if hasattr(other, "value"):
            value = other.value
        else:
            value = other
        return self.value == value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = [phone] if phone else []

    def add_phone(self, phone: Phone):
        if phone in self.phones:
            raise ValueError(f"phone: {phone} is already in record")
        self.phones.append(phone)

    def delete_phone(self, phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            raise ValueError(f"phone: {phone} not exists")

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        try:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
        except ValueError:
            raise ValueError(f"old phone: {phone} not exists")


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, key_name: str):
        result = self.data.get(key_name)
        if self.data.get(key_name) == None:
            raise ValueError("There isn't such record")
        return result


if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("1234567890")
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab["Bill"], Record)
    assert isinstance(ab["Bill"].name, Name)
    assert isinstance(ab["Bill"].phones, list)
    assert isinstance(ab["Bill"].phones[0], Phone)
    assert ab["Bill"].phones[0].value == "1234567890"

    print("All Ok)")
