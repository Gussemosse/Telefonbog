import json
from validate_phonenumber import valider_telefonnummer

# Funktioner

# Telefonbog json fil

def gem_telefonbog():
    with open("telefonbog.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

def læs_telefonbog():
    with open("telefonbog.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Program og hoved funktioner
def add_or_remove_contact():
    add_or_remove = input("Tryk 'a' for tilføjelse af ny kontakt eller 'r' for at slette en kontakt fra telefonbogen: ")
    if add_or_remove == "a":
        new_person = input("Skriv navnet på ny person her:")

        while True:
            new_number = input("Skriv personens nummer her: ")
        
            # Validerer nummeret med funktionen
            if valider_telefonnummer(new_number):
                contacts[new_person] = new_number
                print(f"'{new_person}' blev tilføjet med succes!")
                break
            else:
                print("Ugyldigt telefonnummer. Prøv venligst igen.")

        contacts.update({new_person: new_number})

    if add_or_remove == "r":

        while True:
            delete_contact = input("Skriv navnet på person du vil fjerne her: ")

            if delete_contact not in contacts:
                print("Navn ikke i telefonbog. Prøv venligst igen.")
            else:
                print(f"'{delete_contact}' blev fjernet med succes!")
                del contacts[delete_contact]

def find_contact():
    person = input("Skriv navn på person her: ")
    if person in contacts:
        print(f"{person}'s nummer er: {contacts[person]}")
    else:
        print("Person ikke fundet")

def show_all_contacts():
    print("-----TELEFONBOG-----")
    for key, value in contacts.items(): # Items retunerer et view objekt, som fremviser listen af et dictionaries tuple par.
        mellemrum = value.replace(" ", "") # Fjerner mellemrum, så alle telefonnumrer er ens.
        print(f"{key}: {mellemrum}")

# Læser selve contacts fra json filen, inden loopet længere nede.
contacts = læs_telefonbog()

# Loop
while True:
    # Gemmer nuværende standart dict i json fil.

    print("\n1. Tilføj eller fjern kontakt")
    print("2. Find kontakt")
    print("3. Vis alle kontakter")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_or_remove_contact()

        # Gemmer ændringerne til json filen.
        gem_telefonbog()

    if choice == "2":
        find_contact()

    if choice == "3":
        show_all_contacts()

    if choice == "4":
        break