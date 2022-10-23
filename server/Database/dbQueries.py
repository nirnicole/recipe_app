from Database.dbManager import connection

def get_table(val):
    try:
        with connection.cursor() as cursor:
            # get_number = f"SELECT value FROM numval WHERE number = {int(num)}"
            get_table = f"SELECT * FROM {val}"
            print(get_table)
            cursor.execute(get_table)
            result = cursor.fetchall()
            print(result)
            return result
    except TypeError as e:
        print(e)

def insert_record(record):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT IGNORE INTO recipes values({record})"
            cursor.execute(query)
            connection.commit()
    except TypeError as e:
        print(e)

def ing_exist(table, column, val):
    cur = connection.cursor()
    cur.execute(f"SELECT {column} FROM {table} WHERE {column} = '{val}' LIMIT 1")
    if cur.fetchone():
        return True
    else:
        return False

