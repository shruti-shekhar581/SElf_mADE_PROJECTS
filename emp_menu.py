#For its execution we need to create a table in sql

import sqlite3

TABLENAME = "employees"
DBNAME = "hr.db"

def update_employee(connection):
    print("\nUpdate Employee")
    print("================")
    cur = connection.cursor()
    id = int(input("Enter id :"))
    salary = int(input("Enter new salary :"))

    try:
        cur.execute("update employees set salary = ? where id = ?", (salary, id))
        if cur.rowcount == 1:
            print("Updated Successfully!")
            con.commit()
        else:
            print("Sorry! Employee id not found!")
    except Exception as ex:
        print("Error : ", ex)

    print("\n")


def add_employee(connection):
    print("\nAdd New Employee")
    print("================")
    cur = connection.cursor()
    name = input("Enter name :")
    job = input("Enter job :")
    salary = int(input("Enter salary :"))
    try:
        cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                    (name, job, salary))
        print("Added Employee Successfully!")
        con.commit()  # make insertion permanent
    except Exception as ex:
        print("Error : ", ex)

    cur.close()
    print("\n")


def list_employees(connection):
    print("\nList of Employees")
    print("==================")
    cur = connection.cursor()
    cur.execute(f"select * from {TABLENAME} order by id")  # SQL Command

    for id, name, job, salary in cur.fetchall():
        print(f"{id:2} {name:30} {job:10} {salary:10}")

    cur.close()
    print("\n")


# Connect to DB


try:
    con = sqlite3.connect(DBNAME)
except Exception as ex:
    print("Sorry! Could not connect to database!")
    print("Error  :", ex)
    exit(1)

while True:
    print("Employee Menu")
    print("=============")
    print("1. List Employees")
    print("2. Add Employee")
    print("3. Update Employee")
    print("9. Quit")

    choice = int(input("Enter Choice :"))
    match choice:
        case 1:
            list_employees(con)
        case 2:
            add_employee(con)
        case 3:
            update_employee(con)
        case 9:
            con.close()
            print("Thank you!!")
            exit(0)