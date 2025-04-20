import psycopg2
from config import load_config

def insert(user_name, second_name, last_name, phone_number, config):
    sql = f"""INSERT INTO phone_book(name, second_name, last_name, phone_number) VALUES('{user_name}', '{second_name}', '{last_name}', '{phone_number}') RETURNING person_id"""

    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                rows = cursor.fetchone()
                if rows:
                    person_id = rows[0]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return person_id
    
def query(name, second_name, last_name, config):
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM phone_book WHERE name = '{name}' and second_name = '{second_name}' and last_name = '{last_name}'")
                row = cursor.fetchone()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        return row
    

def update(user_name, second_name, last_name, phone_number, config):
    sql = f""" 
        UPDATE phone_book
        SET phone_number = '{phone_number}'
        WHERE name = '{user_name}' and second_name = '{second_name}' and last_name = '{last_name}'
    """
    try:
        with psycopg2.connect(**config) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    


config = load_config()
user_name = input("Name: ")
second_name = input("Second Name: ")
last_name = input("Surname: ")
phone_number = input("Phone Number: ")
if query(user_name, second_name, last_name, config) == None:
    insert(user_name, second_name, last_name, phone_number, config)
else:
    print("User exists: rewriting data")
    update(user_name, second_name, last_name, phone_number, config)

