import mysql.connector as sql
import os
import getpass
import time

lib = sql.connect(user = 'root', password = 'password', host = 'localhost', database = 'library')
cur = lib.cursor()

def clear():
    os.system('clear')

def welcome():
    clear()
    print("Welcome to our Library Management System\n")

def printMenu():
    clear()
    print("1. Add new Data\n2. Book Management\n3. Run other queries\n4. Exit\n")
    ch = int(input())
    
    if ch == 1:
        printAdd()
    elif ch == 2:
        printBookman()
    elif ch == 3:
        printRunq()
    elif ch == 4:
        exit

def printAdd():
    clear()
    print("1. Add new Book\n2. Add new Member\n3. Add new Author\n4. Add new Publisher\n5. Add new Employee\n6. Exit\n")
    ch = int(input())

    if ch == 1:
        addbook()
    elif ch == 2:
        addmember()
    elif ch == 3:
        addauthor()
    elif ch == 4:
        addpub()
    elif ch == 5:
        addemp()
    elif ch == 6:
        exit

def printBookman():
    clear()
    print("1. Issue a Book\n2. Return a Book\n3. Exit\n")
    ch = int(input())
    
    if ch == 1:
        issueb()
    elif ch == 2:
        retb()
    elif ch == 3:
        exit

def printRunq():
    clear()
    print("")

def runuser():
    clear()
    id = input("Enter Username- ")
    password = getpass.getpass(prompt = 'Enter Password- ')
    if id == 'admin' and password == 'admin':
        return 1
    elif id == 'member' and password == 'member':
        return 2
    elif id == 'employee' and password == 'employee':
        return 3
    else:
        exit

def issueb():
    bid = int(input("Book ID- "))
    mem_id = int(input("Member ID- "))
    
    cur.execute("insert into borrowed values ( %s, %s, '2019-04-24')", (mem_id, bid))
    lib.commit()

    cur.execute("update books set available = available - 1 where book_id = %s", (bid, ))
    lib.commit()

    cur.execute("update member set total_issued = total_issued + 1 where member_id = %s", (mem_id, ))
    lib.commit()

def retb():
    bid = int(input("Book ID- "))
    mem_id = int(input("Member ID- "))
    
    cur.execute("delete from borrowed where book_id = %s and member_id = %s", (bid, mem_id))
    lib.commit()

    cur.execute("update books set available = available + 1 where book_id = %s", (bid, ))
    lib.commit()

    cur.execute("update member set total_issued = total_issued - 1 where member_id = %s", (mem_id, ))
    lib.commit()

def addbook():
    title = input("Title- ")
    genre = input("Genre- ")
    price = int(input("Price- "))
    available = int((input("Available- ")))
    authid = int(input("Author ID- "))
    pubid = int(input("Publisher ID- "))
    
    comm = "insert into books ( title, genre, price, available ) values ( %s, %s, %s, %s);"
    val = (title, genre, price, available)

    cur.execute(comm, val)
    lib.commit()

    cur.execute("select book_id from books where title = %s", title)
    bid = int(cur.fetchone())

    cur.execute("insert into writen values ( %d, %d )", (bid, authid))
    lib.commit

    cur.execute("insert into published values ( %d, %d, %d )", (pubid, bid, authid))
    lib.commit

def addmember():
    name = input("Name- ")
    mem_lev = input("Membership Level- ")
    phone = int(input("Phone- "))
    tot_issue = int((input("Total Issued- ")))
    
    comm = "insert into member ( name, phone, membership_level, total_issued ) values ( %s, %s, %s, %s );"
    val = (name, phone, mem_lev, tot_issue)

    cur.execute(comm, val)
    lib.commit()

def addauthor():
    name = input("Name- ")

    comm = "insert into author ( name ) values ( %s );"
    val = (name, )

    cur.execute(comm, val)
    lib.commit()

def addpub():
    name = input("Name- ")

    comm = "insert into publisher ( name ) values ( %s );"
    val = (name, )

    cur.execute(comm, val)
    lib.commit()

def addemp():
    name = input("Name- ")
    sal = int(input("Salary- "))

    comm = "insert into librarian ( name, salary ) values ( %s, %s );"
    val = (name, sal)

    cur.execute(comm, val)
    lib.commit()

if __name__ == '__main__':
    
    user = runuser()
    welcome()
    time.sleep(10)

    while True:
            if user == 1:
                printMenu()
            elif user == 2:
                printBookman()
            elif user == 3:
                printAdd()
    
    #Do something
