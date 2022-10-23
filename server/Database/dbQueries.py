import json
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





# def create_type(types_pokimon):
#     try:
#         with connection.cursor() as cursor:           
#                 insert_type_pokimon = f"INSERT IGNORE INTO typepokemon values('{types_pokimon}')"
#                 cursor.execute(insert_type_pokimon)
#                 connection.commit()
           
#     except TypeError as e:
#         print(e)


# def create_type_pokimon_to_pokimon(types_pokimon,id_pokimon):
#     try:
#         with connection.cursor() as cursor:           
#            insert_type_pokimon = f"INSERT IGNORE INTO typepokemon_pokemon values('{types_pokimon}',{id_pokimon})"
#            cursor.execute(insert_type_pokimon)
#            connection.commit()          
            

#     except TypeError as e:
#         print(e)


# def create_trainer(name,town):
#     try:
#         with connection.cursor() as cursor:
#             insert_trainer = f"INSERT IGNORE INTO trainer(name_trainer,town) values('{name}','{town}')"            
#             cursor.execute(insert_trainer)
#             connection.commit()
#     except TypeError as e:
#         print(e)

# def create_trainer_pokimon(name_trainer,id_pokimon):
#     try:
#         with connection.cursor() as cursor:
#             insert_trainer = f"INSERT IGNORE INTO trainer_pokemon values('{name_trainer}',{id_pokimon})"            
#             cursor.execute(insert_trainer)
#             connection.commit()
#     except TypeError as e:
#         print(e)


# def create_all_the_data_about_pokimons():
#     for pokimon in pokimon_data_fetures:
#                 create_pokimon(pokimon["id"],
#                 pokimon["name"],                
#                 pokimon["height"],
#                 pokimon["weight"])
                
#                 create_type(pokimon["type"])
#                 create_type_pokimon_to_pokimon(pokimon["type"],pokimon["id"])
#                 for trainer in pokimon["ownedBy"]:                    
#                     create_trainer(trainer["name"],trainer["town"])
#                     create_trainer_pokimon(trainer["name"],pokimon["id"])
                   


# create_all_the_data_about_pokimons()