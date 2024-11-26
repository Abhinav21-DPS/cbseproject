import mysql.connector as ms
from prettytable import PrettyTable

mydb = ms.connect(host="localhost", user="root", password="2112007")
if mydb.is_connected():
    cur = mydb.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS Justice_Prison")
    cur.execute("USE Justice_Prison")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS prisoners (
            id INT PRIMARY KEY,
            name VARCHAR(150) NOT NULL,
            crime VARCHAR(200) NOT NULL,
            penalty INT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS police_officers (
            id INT PRIMARY KEY,
            namex VARCHAR(500) NOT NULL,
            rankx VARCHAR(300) NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS VISITORS (
            visitor_name VARCHAR(20),
            contact_number INT,
            prisoner_name VARCHAR(20)
        )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS INCIDENTS (
        incident_id INT PRIMARY KEY,
        incident_date DATE,
        prisoner_name VARCHAR(200),
        incident_details VARCHAR(200),
        punishment VARCHAR(300)
    )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS medical_records (
        record_id INT PRIMARY KEY,
        prisoner_id INT,
        diagnosis VARCHAR(100),
        treatment VARCHAR(200),
        date_of_treatment DATE,
        doctor_in_charge VARCHAR(100),
        FOREIGN KEY (prisoner_id) REFERENCES prisoners(id))""");

def defaultval_prisoners():
        cur.execute("""INSERT INTO prisoners (id, name, crime, penalty) VALUES
            (1, "Johnson", "Robbery", 3000),
            (2, "William", "War Crime", 10000),
            (3, "Harry", "Assault", 2500),
            (4, "Robert", "Fraud", 1200),
            (5, "Chris", "Narcotics", 7500)
        """)
        mydb.commit()

def defaultval_police_officers():
        cur.execute("""INSERT INTO police_officers (id, namex, rankx) VALUES
            (271, "Marco", "Constable"),
            (365, "Vincent", "Sergeant"),
            (7, "Lewis", "Chief")
        """)
        mydb.commit()

def defaultval_visitors():
        cur.execute("""INSERT INTO visitors (visitor_name, contact_number, prisoner_name) VALUES
            ("Sarah", "056332123", "Johnson"),
            ("Michael", "0558429271", "Charles"),
            ("Andrew", "021123832", "Robert"),
            ("Thomas", "050244332", "Chris")
        """)
        mydb.commit()

def defaultval_incidents():
    cur.execute("""
        INSERT INTO incidents VALUES
            (1, '2024-01-15', 'Johnson', 'Fighting with another inmate', '10 days in isolation'),
            (2, '2024-02-20', 'William', 'Possession of contraband', '30 days loss of privileges'),
            (3, '2024-03-05', 'Harry', 'Attempted escape', '60 days in solitary'),
            (4, '2024-04-12', 'Robert', 'Disrespecting staff', '5 days in isolation'),
            (5, '2024-05-25', 'Chris', 'Altercation with guards', '20 days in solitary')
    """)
    mydb.commit()
def defaultval_medical_records():
        cur.execute("""INSERT INTO medical_records (record_id,prisoner_id,diagnosis,treatment,date_of_treatment,doctor_in_charge) VALUES
            (1,1,"Hypertension","Medication","2024-03-15","Jim Carter"),
            (2,2,"Diabetes","Insulin Therapy","2024-06-22","James Caprio"),
            (3,3,"Fracture","Cast","2024-02-05","Savanah Joser"),
            (4,4,"Asthma","Inhaler","2024-07-18","Jimmy Donaldson"),
            (5,5,"Ulcer","Good Diet","2024-08-25","Karl Jacob")
        """)
        mydb.commit()

cur.execute("SELECT COUNT(*) FROM prisoners")
if cur.fetchone()[0] == 0:
    defaultval_prisoners()
cur.execute("SELECT COUNT(*) FROM police_officers")
if cur.fetchone()[0] == 0:
    defaultval_police_officers()
cur.execute("SELECT COUNT(*) FROM visitors")
if cur.fetchone()[0] == 0:
    defaultval_visitors()
cur.execute("SELECT COUNT(*) FROM incidents")
if cur.fetchone()[0] == 0:
    defaultval_incidents()
cur.execute("SELECT COUNT(*) FROM medical_records")
if cur.fetchone()[0] == 0:
    defaultval_medical_records()
        
print("========================================================================================================")
print('''                              WELCOME TO MY SECURE PRISON DATABASE
                                      By- Abhinav Subodh Menon''')
print("========================================================================================================")

ercount = 0
while True:
    password = eval(input("Type the secure 4 digit code to access the database: "))    
    # Password is 2112
    if password == 2112:
        print("Access Granted.")
        while True:
            choice = eval(input(""" 
            What are you looking for?
            1 - Prisoners Table
            2 - Police Officers Table
            3 - Visitors Table
            4 - Incidents Table
            5 - Medical Records
            6 - Quit Database
            Choice: """))
            if choice == 1:
                print("Loading Prisoners Table...")
                print('''
██████╗░██████╗░██╗░██████╗░█████╗░███╗░░██╗███████╗██████╗░░██████╗
██╔══██╗██╔══██╗██║██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗██╔════╝
██████╔╝██████╔╝██║╚█████╗░██║░░██║██╔██╗██║█████╗░░██████╔╝╚█████╗░
██╔═══╝░██╔══██╗██║░╚═══██╗██║░░██║██║╚████║██╔══╝░░██╔══██╗░╚═══██╗
██║░░░░░██║░░██║██║██████╔╝╚█████╔╝██║░╚███║███████╗██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═════╝░
''')
                while True:
                    print(''' 
                1 - Add Entry or Column
                2 - Delete Entry or Column or Table
                3 - Update Entry
                4 - Search for a record
                5 - Display all Entries
                6 - Quit''')
                    ch = eval(input("Type your choice: "))
                    if ch == 1:
                        chx = eval(input(''' 
                1 - Add Entry
                2 - Add Column
                Choice: '''))
                        if chx == 1:
                            pid = input("Type prisoner id: ")
                            pname = input("Type prisoner name: ")
                            crime = input("Type the crime committed: ")
                            cur.execute('INSERT INTO PRISONERS (id, name, crime) VALUES ("{}", "{}", "{}")'.format(pid, pname, crime))
                            mydb.commit()
                            print("Entry Added.")
                        elif chx == 2:
                            cname = input("Type column name: ")
                            dtype = input("Type data type: ")
                            cur.execute(f"ALTER TABLE PRISONERS ADD {cname} {dtype}")
                            print("Column added.")
                        else:
                            print("Please enter a valid choice")
                    elif ch == 2:
                        chx = eval(input(''' 
                1- Delete Entry
                2 - Delete Column
                3 - Delete Table: '''))    
                        if chx == 1:
                            did = eval(input("Type the the row id that you want to delete: "))
                            cur.execute(f"DELETE FROM PRISONERS WHERE id = {did}")
                            mydb.commit()
                            print("Entry Removed.")
                        elif chx == 2:
                            dname = input("Type the column name you want to delete: ")
                            cur.execute(f"ALTER TABLE PRISONERS DROP COLUMN {dname}")
                            mydb.commit()
                            print("Column deleted.")
                        elif chx == 3:
                            cur.execute("DROP TABLE PRISONERS")
                    elif ch == 3:
                        rid = int(input("Type the row id whose details you want to change: "))
                        change = input(f"What do you want to change for prisoner with ID {rid}? ")
                        changey = input(f"What do you want to change '{change}' to? ")
                        cur.execute(f"UPDATE PRISONERS SET {change} = %s WHERE id = %s", (changey, rid))
                        mydb.commit()
                        print("Record Updated.")
                    elif ch == 4:
                        row = PrettyTable()
                        cur.execute("DESCRIBE PRISONERS")
                        l = []
                        for i in cur:
                            l.append(i[0])
                        rid = int(input("Type the prisoner id: "))
                        cur.execute(f"SELECT * FROM PRISONERS WHERE id = {rid}")
                        row.field_names = l
                        for i in cur:
                            row.add_row(i)
                        print(row)
                    elif ch == 5:
                        table = PrettyTable()
                        cur.execute("DESCRIBE PRISONERS")
                        l = []
                        for i in cur:
                            l.append(i[0])
                        table.field_names = l
                        cur.execute(f"SELECT * FROM PRISONERS")
                        for i in cur:
                            table.add_row(i)
                        print(table)        
                    elif ch == 6:
                        print("Exiting Prisoners Table...")
                        break
                    else:
                        print("Please enter a valid choice.")
            elif choice == 2:
                print("Loading Police Officers Table...")
                print('''
██████╗░░█████╗░██╗░░░░░██╗░█████╗░███████╗  ░█████╗░███████╗███████╗██╗░█████╗░███████╗██████╗░░██████╗
██╔══██╗██╔══██╗██║░░░░░██║██╔══██╗██╔════╝  ██╔══██╗██╔════╝██╔════╝██║██╔══██╗██╔════╝██╔══██╗██╔════╝
██████╔╝██║░░██║██║░░░░░██║██║░░╚═╝█████╗░░  ██║░░██║█████╗░░█████╗░░██║██║░░╚═╝█████╗░░██████╔╝╚█████╗░
██╔═══╝░██║░░██║██║░░░░░██║██║░░██╗██╔══╝░░  ██║░░██║██╔══╝░░██╔══╝░░██║██║░░██╗██╔══╝░░██╔══██╗░╚═══██╗
██║░░░░░╚█████╔╝███████╗██║╚█████╔╝███████╗  ╚█████╔╝██║░░░░░██║░░░░░██║╚█████╔╝███████╗██║░░██║██████╔╝
╚═╝░░░░░░╚════╝░╚══════╝╚═╝░╚════╝░╚══════╝  ░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝╚═════╝░''')
                while True:
                    print(''' 
                    1 - Add Entry or Column
                    2 - Delete Entry or Column or Table
                    3 - Update Entry
                    4 - Search for a record
                    5 - Display all Entries
                    6 - Quit''')
                    ch = eval(input("Type your choice: "))
                    
                    if ch == 1:
                        chx = eval(input(''' 
                    1 - Add Entry
                    2 - Add Column
                    Choice: '''))
                        if chx == 1:
                            officer_id = input("Type officer ID: ")
                            officer_name = input("Type officer name: ")
                            rank = input("Type officer rank: ")
                            cur.execute('INSERT INTO POLICE_OFFICERS (id, namex, rankx) VALUES (%s, %s, %s)', (officer_id, officer_name, rank))
                            mydb.commit()
                            print("Entry Added.")
                        elif chx == 2:
                            cname = input("Type column name: ")
                            dtype = input("Type data type: ")
                            cur.execute(f"ALTER TABLE POLICE_OFFICERS ADD {cname} {dtype}")
                            print("Column added.")
                        else:
                            print("Please enter a valid choice.")
                    
                    elif ch == 2:
                        chx = eval(input(''' 
                    1 - Delete Entry
                    2 - Delete Column
                    3 - Delete Table: '''))    
                        if chx == 1:
                            officer_id = eval(input("Type the officer ID you want to delete: "))
                            cur.execute(f"DELETE FROM POLICE_OFFICERS WHERE id = {officer_id}")
                            mydb.commit()
                            print("Entry Removed.")
                        elif chx == 2:
                            dname = input("Type the column name you want to delete: ")
                            cur.execute(f"ALTER TABLE POLICE_OFFICERS DROP COLUMN {dname}")
                            mydb.commit()
                            print("Column deleted.")
                        elif chx == 3:
                            cur.execute("DROP TABLE POLICE_OFFICERS")
                            mydb.commit()
                            print("Table deleted.")
                    
                    elif ch == 3:
                        officer_id = int(input("Type the officer ID whose details you want to change: "))
                        change = input(f"What do you want to change for officer with ID {officer_id}? ")
                        changey = input(f"What do you want to change '{change}' to? ")
                        cur.execute(f"UPDATE POLICE_OFFICERS SET {change} = %s WHERE id = %s", (changey, officer_id))
                        mydb.commit()
                        print("Record Updated.")
                    
                    elif ch == 4:
                        row = PrettyTable()
                        cur.execute("DESCRIBE POLICE_OFFICERS")
                        l = [i[0] for i in cur]
                        officer_id = int(input("Type the officer ID: "))
                        cur.execute(f"SELECT * FROM POLICE_OFFICERS WHERE id = {officer_id}")
                        row.field_names = l
                        for i in cur:
                            row.add_row(i)
                        print(row)
                    
                    elif ch == 5:
                        table = PrettyTable()
                        cur.execute("DESCRIBE POLICE_OFFICERS")
                        l = [i[0] for i in cur]
                        table.field_names = l
                        cur.execute("SELECT * FROM POLICE_OFFICERS")
                        for i in cur:
                            table.add_row(i)
                        print(table)
                    
                    elif ch == 6:
                        print("Exiting Police Officers Table...")
                        break
                    else:
                        print("Please enter a valid choice.")
            elif choice == 3:
                print("Loading Visitors Table...")
                print('''
██╗░░░██╗██╗░██████╗██╗████████╗░█████╗░██████╗░░██████╗
██║░░░██║██║██╔════╝██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
╚██╗░██╔╝██║╚█████╗░██║░░░██║░░░██║░░██║██████╔╝╚█████╗░
░╚████╔╝░██║░╚═══██╗██║░░░██║░░░██║░░██║██╔══██╗░╚═══██╗
░░╚██╔╝░░██║██████╔╝██║░░░██║░░░╚█████╔╝██║░░██║██████╔╝
░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░''')
                while True:
                    print(''' 
                    1 - Add Entry or Column
                    2 - Delete Entry or Column or Table
                    3 - Update Entry
                    4 - Search for a visitor record
                    5 - Display all Entries
                    6 - Quit''')
                    ch = eval(input("Type your choice: "))

                    if ch == 1:
                        chx = eval(input(''' 
                    1 - Add Entry
                    2 - Add Column
                    Choice: '''))
                        if chx == 1:
                            visitor_name = input("Type visitor's name: ")
                            contact_number = input("Type visitor's contact number: ")
                            prisoner_name = input("Type the name of the prisoner they are visiting: ")
                            cur.execute('INSERT INTO VISITORS (visitor_name, contact_number, prisoner_name) VALUES (%s, %s, %s)', (visitor_name, contact_number, prisoner_name))
                            mydb.commit()
                            print("Entry Added.")
                        elif chx == 2:
                            cname = input("Type column name: ")
                            dtype = input("Type data type: ")
                            cur.execute(f"ALTER TABLE VISITORS ADD {cname} {dtype}")
                            print("Column added.")
                        else:
                            print("Please enter a valid choice.")
                    
                    elif ch == 2:
                        chx = eval(input(''' 
                    1 - Delete Entry
                    2 - Delete Column
                    3 - Delete Table: '''))    
                        if chx == 1:
                           visitor_namex = input("Type the visitor name you want to delete: ")
                           cur.execute("DELETE FROM VISITORS WHERE visitor_name = %s", (visitor_namex,))
                           mydb.commit()
                           print("Entry Removed.")
                        elif chx == 2:
                            dname = input("Type the column name you want to delete: ")
                            cur.execute(f"ALTER TABLE VISITORS DROP COLUMN {dname}")
                            mydb.commit()
                            print("Column deleted.")
                        elif chx == 3:
                            cur.execute("DROP TABLE VISITORS")
                            mydb.commit()
                            print("Table deleted.")

                    elif ch == 3:
                        visitor_name = input("Type the visitor ID whose details you want to change: ")
                        change = input(f"What do you want to change for visitor with name {visitor_name}? ")
                        changey = input(f"What do you want to change '{change}' to? ")
                        cur.execute(f"UPDATE VISITORS SET {change} = %s WHERE visitor_name = %s", (changey, visitor_name))
                        mydb.commit()
                        print("Record Updated.")

                    elif ch == 4:
                        row = PrettyTable()
                        cur.execute("DESCRIBE VISITORS")
                        l = [i[0] for i in cur.fetchall()]
                        visitor_namex = input("Type the visitor name: ")
                        cur.execute("SELECT * FROM VISITORS WHERE visitor_name = %s", (visitor_namex,))
                        row.field_names = l
                        for i in cur:
                            row.add_row(i)
                        print(row)

                    elif ch == 5:
                        table = PrettyTable()
                        cur.execute("DESCRIBE VISITORS")
                        l = [i[0] for i in cur]
                        table.field_names = l
                        cur.execute("SELECT * FROM VISITORS")
                        for i in cur:
                            table.add_row(i)
                        print(table)

                    elif ch == 6:
                        print("Exiting Visitors Table...")
                        break
                    else:
                        print("Please enter a valid choice.")
            
            elif choice == 4:
                print("Loading Incidents Table...")
                print('''
██╗███╗░░██╗░█████╗░██╗██████╗░███████╗███╗░░██╗████████╗░██████╗
██║████╗░██║██╔══██╗██║██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔════╝
██║██╔██╗██║██║░░╚═╝██║██║░░██║█████╗░░██╔██╗██║░░░██║░░░╚█████╗░
██║██║╚████║██║░░██╗██║██║░░██║██╔══╝░░██║╚████║░░░██║░░░░╚═══██╗
██║██║░╚███║╚█████╔╝██║██████╔╝███████╗██║░╚███║░░░██║░░░██████╔╝
╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░''')
                while True:
                    print(''' 
                    1 - Add Entry or Column
                    2 - Delete Entry or Column or Table
                    3 - Update Entry
                    4 - Search for an incident record
                    5 - Display all Entries
                    6 - Quit''')
                    ch = eval(input("Type your choice: "))
                    
                    if ch == 1:
                        chx = eval(input(''' 
                    1 - Add Entry
                    2 - Add Column
                    Choice: '''))
                        if chx == 1:
                            incident_id = int(input("Type incident id: ")) 
                            incident_date = input("Type incident date (YYYY-MM-DD): ")  
                            prisoner_name = input("Type name of prisoner who committed the incident: ")
                            incident_details = input("Type incident details: ")
                            punishment = input("Type the punishment the offender: ")
                            cur.execute("""
                                INSERT INTO INCIDENTS (incident_id, incident_date, prisoner_name, incident_details, punishment)
                                VALUES (%s, %s, %s, %s, %s)
                            """, (incident_id, incident_date, prisoner_name, incident_details, punishment))
                            mydb.commit()
                            print("Entry Added.")
                        elif chx == 2:
                            cname = input("Type column name: ").strip() 
                            dtype = input("Type data type: ").strip() 
                            
                            try:
                                query = f"ALTER TABLE INCIDENTS ADD COLUMN {cname} {dtype}"
                                cur.execute(query)
                                mydb.commit()
                                print("Column Added.")
                            except:
                                print("Error")
                        else:
                            print("Please enter a valid choice.")
                    
                    elif ch == 2:
                        chx = eval(input(''' 
                    1 - Delete Entry
                    2 - Delete Column
                    3 - Delete Table: '''))    
                        if chx == 1:
                            incident_id = int(input("Type the incident ID you want to delete: "))  
                            cur.execute("DELETE FROM INCIDENTS WHERE incident_id = %s", (incident_id,)) 
                            mydb.commit()
                            print("Entry Removed.")

                  
                        elif chx == 2:
                            dname = input("Type the column name you want to delete: ")
                            cur.execute(f"ALTER TABLE INCIDENTS DROP COLUMN {dname}")
                            mydb.commit()
                            print("Column deleted.")
                        elif chx == 3:
                            cur.execute("DROP TABLE INCIDENTS")
                            mydb.commit()
                            print("Table deleted.")
                    elif ch==3:
                         incident_id = int(input("Type the incident ID whose details you want to change: "))
                         change = input(f"What do you want to change for incident with ID {incident_id}? ")
                         changey = input(f"What do you want to change '{change}' to? ")
                         cur.execute(f"UPDATE INCIDENTS SET {change} = %s WHERE incident_id = %s", (changey, incident_id))
                         mydb.commit()
                         print("Record Updated.")
                    
                     
                                                
                    elif ch == 4:
                        row = PrettyTable()
                        cur.execute("DESCRIBE INCIDENTS")
                        l = [i[0] for i in cur]
                        incident_id = int(input("Type the incident ID: "))
                        cur.execute(f"SELECT * FROM INCIDENTS WHERE incident_id = {incident_id}")
                        row.field_names = l
                        for i in cur:
                            row.add_row(i)
                        print(row)
                    
                    elif ch == 5:
                        table = PrettyTable()
                        cur.execute("DESCRIBE INCIDENTS")
                        l = [i[0] for i in cur]
                        table.field_names = l
                        cur.execute("SELECT * FROM INCIDENTS")
                        for i in cur:
                            table.add_row(i)
                        print(table)

                    elif ch == 6:
                        print("Exiting Incidents Table...")
                        break
                    else:
                        print("Please enter a valid choice.")
            elif choice == 5:
                print("Loading Medical Records Table...")
                print('''
███╗░░░███╗███████╗██████╗░██╗░█████╗░░█████╗░██╗░░░░░  ██████╗░███████╗░█████╗░░█████╗░██████╗░██████╗░░██████╗
████╗░████║██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██╔████╔██║█████╗░░██║░░██║██║██║░░╚═╝███████║██║░░░░░  ██████╔╝█████╗░░██║░░╚═╝██║░░██║██████╔╝██║░░██║╚█████╗░
██║╚██╔╝██║██╔══╝░░██║░░██║██║██║░░██╗██╔══██║██║░░░░░  ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██╔══██╗██║░░██║░╚═══██╗
██║░╚═╝░██║███████╗██████╔╝██║╚█████╔╝██║░░██║███████╗  ██║░░██║███████╗╚█████╔╝╚█████╔╝██║░░██║██████╔╝██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝  ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░''')
                while True:
                    print(''' 
                    1 - Add Entry or Column
                    2 - Delete Entry or Column or Table
                    3 - Update Entry
                    4 - Search for a record
                    5 - Display all Entries
                    6 - Quit''')
                    ch = eval(input("Type your choice: "))
                    
                    if ch == 1:
                        chx = eval(input(''' 
                    1 - Add Entry
                    2 - Add Column
                    Choice: '''))
                        if chx == 1:
                            record_id = int(input("Type record id: "))  
                            prisoner_id = int(input("Type prisoner id: "))  
                            diagnosis = input("Type diagnosis of prisoner: ")
                            treatment = input("Type treatment to be done: ")
                            date_of_treatment = input("Type date of treatment (YYYY-MM-DD): ") 
                            doctor_in_charge = input("Type name of doctor in charge: ")
                            query = '''
                                INSERT INTO medical_records 
                                (record_id, prisoner_id, diagnosis, treatment, date_of_treatment, doctor_in_charge)
                                VALUES (%s, %s, %s, %s, %s, %s)
                            '''
                            values = (record_id, prisoner_id, diagnosis, treatment, date_of_treatment, doctor_in_charge)
                            try:
                                cur.execute(query, values)
                                mydb.commit()
                                print("Entry Added.")
                            except Exception as e:
                                print("Record not found in prison database")
                        elif chx == 2:
                            cname = input("Type column name: ")
                            dtype = input("Type data type: ")
                            cur.execute(f"ALTER TABLE medical_records ADD {cname} {dtype}")
                            print("Column added.")
                        else:
                            print("Please enter a valid choice.")
                    
                    elif ch == 2:
                        chx = eval(input(''' 
                    1 - Delete Entry
                    2 - Delete Column
                    3 - Delete Table: '''))    
                        if chx == 1:
                            record_id = eval(input("Type the record ID you want to delete: "))
                            cur.execute(f"DELETE FROM medical_records WHERE record_id = {record_id}")
                            mydb.commit()
                            print("Entry Removed.")
                        elif chx == 2:
                            dname = input("Type the column name you want to delete: ")
                            cur.execute(f"ALTER TABLE medical_records DROP COLUMN {dname}")
                            mydb.commit()
                            print("Column deleted.")
                        elif chx == 3:
                            cur.execute("DROP TABLE medical_records")
                            mydb.commit()
                            print("Table deleted.")
                    
                    elif ch == 3:
                        record_id = int(input("Type the record ID whose details you want to change: "))
                        change = input(f"What do you want to change for officer with ID {record_id}? ")
                        changey = input(f"What do you want to change '{change}' to? ")
                        cur.execute(f"UPDATE medical_records SET {change} = %s WHERE record_id = %s", (changey, record_id))
                        mydb.commit()
                        print("Record Updated.")
                    
                    elif ch == 4:
                        row = PrettyTable()
                        cur.execute("DESCRIBE medical_records")
                        l = [i[0] for i in cur]
                        record_id = int(input("Type the record ID: "))
                        cur.execute(f"SELECT * FROM medical_records WHERE record_id = {record_id}")
                        row.field_names = l
                        for i in cur:
                            row.add_row(i)
                        print(row)
                    
                    elif ch == 5:
                        table = PrettyTable()
                        cur.execute("DESCRIBE medical_records")
                        l = [i[0] for i in cur]
                        table.field_names = l
                        cur.execute("SELECT * FROM medical_records")
                        for i in cur:
                            table.add_row(i)
                        print(table)
                    
                    elif ch == 6:
                        print("Exiting Medical Records Table...")
                        break
                    else:
                        print("Please enter a valid choice.")
            
            elif choice == 6:
                print("Exiting Database...")
                print('''
 _____ _                 _     __   __                 ______   _______ _ _ _ 
|_   _| |__   __ _ _ __ | | __ \ \ / /__  _   _       | __ ) \ / / ____| | | |
  | | | '_ \ / _` | '_ \| |/ /  \ V / _ \| | | |      |  _ \\ V /|  _| | | | |
  | | | | | | (_| | | | |   <    | | (_) | |_| |      | |_) || | | |___|_|_|_|
  |_| |_| |_|\__,_|_| |_|_|\_\   |_|\___/ \__,_|      |____/ |_| |_____(_|_|_)
  ''')
                quit()
       
            else:
                print("Please enter a valid choice.")
    else:
        ercount += 1
        print("Wrong Password. Try Again.")
        if ercount > 2:
            print("Access Denied.")
            break

cur.close()
mydb.close()
