import json
from psycopg2 import DatabaseError
from update import insert, update, query
from config import load_config

config = load_config()

with open("contacts.json", "r") as data:
    contacts_data = json.load(data)  # Load full JSON (dict)
    contacts_list = contacts_data["contacts"]  # Extract the list

for contact in contacts_list:  # Now loop over the list
    try:
        if query(contact["name"], contact["second_name"], contact["last_name"], config) == None:
            print(f"New Data: {contact['name']}")
            insert(contact["name"], contact["second_name"], contact["last_name"], contact["phone_number"], config)
        else:
            print(f"\n{contact} \nExists \n")
            update(contact["name"], contact["second_name"], contact["last_name"], contact["phone_number"], config)
    except (DatabaseError, Exception) as error:
        print(error)

