import sqlite3

def create_db():
    connection = sqlite3.connect('vrm.db')
    cursor = connection.cursor()

    basetable_query = ''' CREATE TABLE IF NOT EXISTS BaseUser(
                            id INTEGER PRIMARY KEY,
                            user_name VARCHAR(25),
                            email VARCHAR(50),
                            phone_number INTEGER,
                            address VARCHAR(100)
                        ); '''
    cursor.execute(basetable_query)

    client_query = ''' CREATE TABLE IF NOT EXISTS Client( 
                        base_id INT references BaseUser(id) 
                        ); '''
    cursor.execute(client_query)

    mechanic_query = ''' CREATE TABLE IF NOT EXISTS Mechanic(
                            title VARCHAR(25),
                            base_id INT references BaseUser(id)
                        ); '''
    cursor.execute(mechanic_query)

    service_query = ''' CREATE TABLE IF NOT EXISTS Service(
                            id INT PRIMARY KEY,
                            name VARCHAR(25)
                        ); '''
    cursor.execute(service_query)

    mechanic_service_query = ''' CREATE TABLE IF NOT EXISTS MechanicService(
                                    id INT PRIMARY KEY,
                                    mechanic_id INT references Mechanic(base_id),
                                    service_id INT references Service(id)
                                ); '''
    cursor.execute(mechanic_service_query)

    repair_hour_query = ''' CREATE TABLE IF NOT EXISTS RepairHour(
                                id INT PRIMARY KEY, 
                                date VARCHAR(25),
                                start_hour VARCHAR(25),
                                vehicle VARCHAR(25) references Vehicle(id),
                                bill REAL
                            ); '''
    cursor.execute(repair_hour_query)

    vehicle_query = ''' CREATE TABLE IF NOT EXISTS Vehicle(
                            id INT PRIMARY KEY,
                            category VARCHAR(25),
                            make VARCHAR(25),
                            model VARCHAR(25),
                            register_number VARCHAR(25),
                            gear_box VARCHAR(25),
                            owner VARCHAR(25) references Client(base_id)
                            ); '''
    cursor.execute(vehicle_query)
       

    connection.commit()
    connection.close()

def main():
    pass

if __name__ == "__main__":
    main()