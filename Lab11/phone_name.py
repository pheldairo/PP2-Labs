import psycopg2
from config import load_config
def get_records_by_pattern(pattern):
    records = []
    sql = """ SELECT person_id, name, last_name, phone_number FROM phone_book
              WHERE name ILIKE %s OR last_name ILIKE %s OR phone_number ILIKE %s """
    config = None
    conn = None
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        search_pattern = f'%{pattern}%'
        cur.execute(sql, (search_pattern, search_pattern, search_pattern))
        records = cur.fetchall()
        cur.close()
    except (psycopg2.DatabaseError, Exception) as error:
        print(f"Error connecting to or querying database: {error}")
    finally:
        if conn is not None:
            conn.close()
    return records


    # Example: Get records where name, surname, or phone contains 'an'
search_pattern = input("Enter pattern: ")
matched_records = get_records_by_pattern(search_pattern)
if matched_records:
    print("\nMatching records found:")
    for record in matched_records:
        # Assuming record format is (user_id, first_name, last_name, phone_number)
        print(f"ID: {record[0]}, Name: {record[1]} {record[2]}, Phone: {record[3]}")
else:
    print(f"No records found matching '{search_pattern}'.")


