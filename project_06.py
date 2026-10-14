def create_contacts():
    contacts = {}
    contacts["Maya"] = "555-0101"
    contacts["Noah"] = "555-0102"
    return contacts


def search(contacts, name):
    return contacts.get(name, "Not found")


def main():
    contacts = create_contacts()
    print(search(contacts, "Maya"))
    print(search(contacts, "Sam"))


if __name__ == "__main__":
    main()
