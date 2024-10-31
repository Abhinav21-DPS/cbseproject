import mysql.connector as ms
from prettytable import PrettyTable

mydb = ms.connect(host="localhost", user="root", password="______")
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
            id INT PRIMARY KEY,
            visitor_name VARCHAR(20),
            contact_number INT,
            prisoner_name VARCHAR(20)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS INCIDENTS (
            id INT PRIMARY KEY,
            incident_date DATE,
            prisoner_name VARCHAR(200),
            incident_details VARCHAR(200),
            punishment VARCHAR(300)
        )
    """)
def defaultval_prisoners():
    cur.execute("""INSERT INTO PRISONERS VALUES
               ('2024-01-15', 'Johnson', 'Fighting with another inmate', '10 days in isolation'),
               ('2024-02-20', 'William', 'Possession of contraband', '30 days loss of privileges'),
               ('2024-03-05', 'Harry', 'Attempted escape', '60 days in solitary'),
               ('2024-04-12', 'Robert', 'Disrespecting staff', '5 days in isolation'),
               ('2024-05-25', 'Chris', 'Altercation with guards', '20 days in solitary');
               """)
def defaultval_police_officers():
    cur.execute("""INSERT INTO police_officers VALUES
               (271,"Marco","Constable"),
               (365,"Vincent","Sergeant");
               (7,"Lewis","Cheif");
               """)
def defaultval_visitors():
    cur.execute("""INSERT INTO VISITORS VALUES
               ("Sarah",056332123,"Johnson"),
               ("Miachel",0558429271,"Charles");
               ("Andrew",021123832,"Robert");
               ("Thomas",050244332,"Chris");
               """)
def defaultval_incidents():
    cur.execute("""INSERT INTO INCIDENTS VALUES
               (1,"Johnson","Robbery",3000),
               (2,"William","War Crime",10000);
               (3,"Harry","Assault",2500);
               (4,"Robert","Fraud",1200);
               (5,"Chris","Narcotics",7500);
               """)

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
        
print("================================================================================")
print('''                       WELCOME TO MY SECURE PRISON DATABASE
                                By- Abhinav Subodh Menon''')
print("================================================================================")

ercount = 0
while True:
    password = eval(input("Type the secure 4 digit code to access the database: "))    
    # 2112
    if password == 2112:
        print("Access Granted.")
        while True:
            choice = eval(input(""" 
            What are you looking for?
            1 - Prisoners Table
            2 - Police Officers Table
            3 - Visitors Table
            4 - Incidents Table
            5 - Quit Database
            Choice: """))
            if choice == 1:
                print("Loading Prisoners Table...")
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
                            defx = input("Type default value: ")
                            if not defx.isdigit():
                                defx = f"'{defx}'"
                            cur.execute(f"ALTER TABLE PRISONERS ADD {cname} {dtype} DEFAULT {defx}")
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
                            defx = input("Type default value: ")
                            if not defx.isdigit():
                                defx = f"'{defx}'"
                            cur.execute(f"ALTER TABLE POLICE_OFFICERS ADD {cname} {dtype} DEFAULT {defx}")
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
                            defx = input("Type default value: ")
                            if not defx.isdigit():
                                defx = f"'{defx}'"
                            cur.execute(f"ALTER TABLE VISITORS ADD {cname} {dtype} DEFAULT {defx}")
                            print("Column added.")
                        else:
                            print("Please enter a valid choice.")
                    
                    elif ch == 2:
                        chx = eval(input(''' 
                    1 - Delete Entry
                    2 - Delete Column
                    3 - Delete Table: '''))    
                        if chx == 1:
                            visitor_id = eval(input("Type the visitor ID you want to delete: "))
                            cur.execute(f"DELETE FROM VISITORS WHERE id = {visitor_id}")
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
                        visitor_id = int(input("Type the visitor ID whose details you want to change: "))
                        change = input(f"What do you want to change for visitor with ID {visitor_id}? ")
                        changey = input(f"What do you want to change '{change}' to? ")
                        cur.execute(f"UPDATE VISITORS SET {change} = %s WHERE id = %s", (changey, visitor_id))
                        mydb.commit()
                        print("Record Updated.")

                    elif ch == 4:
                        row = PrettyTable()
                        cur.execute("DESCRIBE VISITORS")
                        l = [i[0] for i in cur]
                        visitor_id = int(input("Type the visitor ID: "))
                        cur.execute(f"SELECT * FROM VISITORS WHERE id = {visitor_id}")
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
                            incident_date = input("Type incident date: ")
                            prisoner_name  = input("Type name of prisoner who committed the incident: ")
                            incident_details = input("Type incident details: ")
                            punishment = input("Type the punishment the offender: ")
                            cur.execute('INSERT INTO INCIDENTS (incident_date,prisoner_name, incident_details,punishment) VALUES (%s, %s,%s,%s)', (incident_date,prisoner_name, incident_details,punishment))
                            mydb.commit()
                            print("Entry Added.")
                        elif chx == 2:
                            cname = input("Type column name: ")
                            dtype = input("Type data type: ")
                            defx = input("Type default value: ")
                            if not defx.isdigit():
                                defx = f"'{defx}'"
                            cur.execute(f"ALTER TABLE INCIDENTS ADD {cname} {dtype} DEFAULT {defx}")
                            print("Column added.")
                        else:
                            print("Please enter a valid choice.")
                    
                    elif ch == 2:
                        chx = eval(input(''' 
                    1 - Delete Entry
                    2 - Delete Column
                    3 - Delete Table: '''))    
                        if chx == 1:
                            incident_id = eval(input("Type the incident ID you want to delete: "))
                            cur.execute(f"DELETE FROM INCIDENTS WHERE id = {incident_id}")
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
                    
                    elif ch == 3:
                        incident_id = int(input("Type the incident ID whose details you want to change: "))
                        change = input(f"What do you want to change for incident with ID {incident_id}? ")
                        changey = input(f"What do you want to change '{change}' to? ")
                        cur.execute(f"UPDATE INCIDENTS SET {change} = %s WHERE id = %s", (changey, incident_id))
                        mydb.commit()
                        print("Record Updated.")
                    
                    elif ch == 4:
                        row = PrettyTable()
                        cur.execute("DESCRIBE INCIDENTS")
                        l = [i[0] for i in cur]
                        incident_id = int(input("Type the incident ID: "))
                        cur.execute(f"SELECT * FROM INCIDENTS WHERE id = {incident_id}")
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
                print("Exiting Database...")
                break
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
