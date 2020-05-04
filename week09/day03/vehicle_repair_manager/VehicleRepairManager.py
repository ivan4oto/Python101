import sqlite3
from tables_setup import create_db
from general_cmds import create_user

def check_user(*, user_name):
    connection = sqlite3.connect('vrm.db')
    cursor = connection.cursor()
    select_user_query = f'''
        SELECT user_name, Client.base_id AS client_id, Mechanic.base_id as mechanic_id FROM BaseUser 
        LEFT OUTER JOIN Mechanic ON Mechanic.base_id = BaseUser.id 
        LEFT OUTER JOIN Client ON Client.base_id  = BaseUser.id 
        WHERE user_name = "{user_name}";   
    '''
    cursor.execute(select_user_query)
    user = cursor.fetchall()
    if user == []:
        return None
    elif user[0][1] != None and user[0][2] == None:
        return 'client'
    elif user[0][1] == None and user[0][2] != None:
        return 'mechanic'

def quit_program():
    pass



def main():
    create_db()
    user = input('Hello, provide an username:\n')
    user_type = check_user(user_name = user)
    if user_type == None:
        print('Unknown user !')
        n = True
        while n:
            decision = input('Would you like to create new user ?\n')
            if decision.lower() == 'yes':
                usertype = input('Are you a client or mechanic ?\n')
                username = input('Provide user_name:\n')
                phone = input('Provide phone_number:\n')
                mail = input('Provide email:\n')
                adress = input('Provide adress:\n')
                create_user(user_type = usertype, user_name = username, user_phone = phone, user_mail = mail, user_adress = adress)
                print(f'\nThank you, {username}!\nWelcome to Vehicle Services !\nNext time you try to login, provide your user_name !')
                n = False
            elif decision.lower() == 'no':
                break
            else:
                print('wrong command !')
                pass
            

    
if __name__ == "__main__":
    main()