import psycopg2
from config import load_config

user = input("Name: ")
phone_num = input("Phone: ")
def delete_by_username_or_phone(username=None, phone=None):
    config = load_config()
    try:
        connection = psycopg2.connect(**config['database'])
        cursor = connection.cursor()

        if username:
            cursor.execute("DELETE FROM your_table_name WHERE username = %s", (username,))
        elif phone:
            cursor.execute("DELETE FROM your_table_name WHERE phone = %s", (phone,))
        else:
            print("Please provide either a username or phone to delete.")

        connection.commit()
        print("Record deleted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error while deleting record:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

delete_by_username_or_phone(user, phone_num)