import sqlite3


def create_table(name):
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()
    cursor.execute(
        f'''
        CREATE TABLE IF NOT EXISTS "{name}" 
            ( 
            id INTEGER PRIMARY KEY UNIQUE NOT NULL, 
            full_name VARCHAR(25) UNIQUE NOT NULL, 
            email VARCHAR(30) UNIQUE NOT NULL, 
            age INTEGER NOT NULL, 
            phone VARCHAR(25) NOT NULL,  
            additional_info TEXT 
            ); 
        '''
        )
    connection.commit()
    connection.close()

def add_card(full_name, email, age, phone, additional_info, tablename):
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()
    insert_query = f'''
        INSERT INTO {tablename} (full_name, email, age, phone, additional_info) 
        VALUES ( ? , ? , ? , ? , ? );
        '''
    cursor.execute(insert_query, (full_name, email, age, phone, additional_info))    
    connection.commit()
    connection.close()

def list_cards(tablename):
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT * FROM {tablename}        
        """)

    users_data = cursor.fetchall()

    n = 1
    for i in users_data:
        print(f'{n}. ID: {i[0]}, Email: {i[2]}, Full name: {i[1]}')
        n += 1

    connection.commit()
    connection.close()

def delete_card(id, tablename):
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()
    cursor.execute(f"""
        DELETE FROM  {tablename}   
        WHERE id = {id}
        """)
    connection.commit()
    connection.close()

def get_card(id, tablename):
    connection = sqlite3.connect('bcc.db')
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT * FROM {tablename}
        WHERE id = {id}
    """)
    user_data = cursor.fetchall()

    print(f''' 
        Contact info:

        #############
        ID: {user_data[0][0]},
        Full name: {user_data[0][1]},
        Email: {user_data[0][2]},
        Age: {user_data[0][3]},
        Phone: {user_data[0][4]},
        Additional info: {user_data[0][5]}
        #############    
    ''')


    connection.commit()
    connection.close()

def help_cards():
    print('''
    #############
    ###Options###
    #############

    1. `add` - insert new business card
    2. `list` - list all business cards
    3. `delete` - delete a certain business card (`ID` is required)
    4. `get` - display full information for a certain business card (`ID` is required)
    5. `help` - list all available options
    
    ''')

    

def main():

    tablename = input('enter a table: ')

    print('Hello! This is your business card catalog. What would you like? (enter "help" to list all available options)')
    command = input('Enter command: ')
    
    if command == 'help':
        help_cards()

    elif command == 'add':
        username = input('Enter user name: ')
        email = input('Enter email: ')
        age = input('Enter age: ')
        phone = input('Enter phone: ')
        info = input('Enter additional info: ')

        add_card(username, email, age, phone, info, tablename)



    elif command == 'list':
        list_cards(tablename)

    elif command == 'get':
        requested_id = input('Enter id: ')
        get_card(requested_id, tablename)

    elif command == 'delete':
        pass

    

if __name__ == "__main__":
    main()