contacts = {
    "Anna": "23456789",
    "Bjørn": "99887766",
    "Clara": "11223344"
}

# Funktioner
def add_contact():
    new_person = input("Skriv navnet på ny person her:")
    new_number = input("Skriv personens nummer her: ")

    new_data = {}
    new_data.update({new_person: new_number})

    contacts.update(new_data)

def find_contact():
    person = input("Skriv navn på person her: ")
    if person in contacts:
        print(f"{person}'s nummer er: {contacts[person]}")
    else:
        print("Person not found")

def show_all_contacts():
    for key, value in contacts.items(): # Items retunerer et view objekt, som fremviser listen af et dictionaries tuple par.
        print(f"{key}: {value}")

# Loop
while True:
    print("\n1. Add contact")
    print("2. Find contact")
    print("3. Show all contacts")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()

    if choice == "2":
        find_contact()

    if choice == "3":
        show_all_contacts()

    if choice == "4":
        break