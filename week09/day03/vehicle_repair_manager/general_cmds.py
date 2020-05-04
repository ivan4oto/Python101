import sqlite3

def create_user(*, user_type, user_name, user_phone, user_mail, user_adress):
    connection = sqlite3.connect('vrm.db')
    cursor = connection.cursor()

    insert_query_user = '''
    INSERT INTO BaseUser (user_name, email, phone_number, address)
    VALUES ( ? , ? , ? , ? );            
    '''

    cursor.execute(insert_query_user, (user_name, user_phone, user_mail, user_adress))

    cursor.execute(f'''
        SELECT id FROM BaseUser
        WHERE user_name = "{user_name}";
    ''')
    user_id = cursor.fetchall()[0][0]

    if user_type.lower() == 'client':
        insert_query_client = f'''
        INSERT INTO Client (base_id)
        VALUES ({user_id});
        '''
        cursor.execute(insert_query_client)
    
    elif user_type.lower() == 'mechanic':
        insert_query_client = f'''
        INSERT INTO Mechanic (base_id, title)
        VALUES ({user_id}, "mechanic");
        '''
        cursor.execute(insert_query_client)

    connection.commit()
    connection.close()

def add_vehicle(*, category, make, model, register_number, gear_box, owner):
    connection = sqlite3.connect('vrm.db')
    cursor = connection.cursor()
    insert_query_car = '''
    INSERT INTO VEHICLE (category, make, model, register_number, gear_box, owner):
    VALUES ( ? , ? , ? , ? , ? , ? );
    '''

    cursor.execute(insert_query_car,(category, make, model, register_number, gear_box, owner))
    connection.commit()
    connection.close()

def add_repair_hour(*, date, start_hour, vehicle, bill, mechanic_service):
    connection = sqlite3.connect()
    cursor = connection.cursor()
    insert_query_hour = '''
    INSERT INTO RepairHour(date, start_hour, vehicle, bill, mechanic_service)
    VALUES( ? , ? , ? , ? , ? );    
    '''
    cursor.execute(insert_query_hour,(date, start_hour, vehicle, bill, mechanic_service))
    connection.commit()
    connection.close()

    
def list_all_free_hours():
    connection = sqlite3.connect()
    cursor = connection.cursor()
    cursor.execute('''
    SELECT * FROM RepairHour
    WHERE Vehicle IS NULL;
    ''')
    connection.commit()
    connection.close()

def list_free_hours(*, date):
    connection = sqlite3.connect()
    cursor = connection.cursor()
    list_hours_query = '''
    SELECT * FROM RepairHour
    WHERE VEHICLE IS NULL AND DATE = " ? ";
    '''
    cursor.execute(list_hours_query, (date))
    connection.commit()
    connection.close()






def main():
    pass


if __name__ == "__main__":
    main()