import pymysql

# create DB
try:
    initial_connection = pymysql.connect(
        host="localhost",
        user="root",
        password=""
    )
    print("creating data base...")
    initial_connection.cursor().execute('create database recipes_app')
    print("data base created successfully")

except Exception: 
    print("data base already exists!")

# create tables
try:
    initial_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
    print("creating value table...")
    initial_connection.cursor().execute('create table dairy(dairy_ingredients varchar(255))')
    initial_connection.commit()
    initial_connection.cursor().execute('create table gluten(gluten_ingredients varchar(255))')
    initial_connection.commit()
    print("table created successfully")
except Exception: 
    print("tables already exists!")

#add ingridients:
try:
    initial_connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="recipes_app",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    with initial_connection.cursor() as cursor:
        print("inserting values...")
        dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
        gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]
        for dairy in dairy_ingredients:
            cursor.execute(f"INSERT IGNORE INTO dairy(dairy_ingredients) values('{dairy}')")
            initial_connection.commit()

        get_number = f"SELECT * FROM dairy"
        print(get_number)
        cursor.execute(get_number)
        result = cursor.fetchall()
        print(result)

        for gluten in gluten_ingredients:
            cursor.execute(f"INSERT IGNORE INTO gluten(gluten_ingredients) values('{gluten}')")   
            initial_connection.commit()

        get_number = f"SELECT * FROM gluten"
        print(get_number)
        cursor.execute(get_number)
        result = cursor.fetchall()
        print(result)    
            
        print("Done!")    
except Exception: 
    print(Exception.args[0])
    print("coudlnt insert values!")

