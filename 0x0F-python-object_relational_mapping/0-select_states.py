#!/usr/bin/python3
''' script that lists all states from database hbtn_0e_0_usa '''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    ''' connects to the database '''
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    ''' cursor object '''
    cur = db.cursor()
    
    ''' SQL Queries execution with cursor object ''' 
    cur.execute("SELECT * FROM states ORDER BY id")

    ''' fetch all result '''
    result = cur.fetchall()
    for i in result:
        print(i)
    cur.close()
    db.close()
