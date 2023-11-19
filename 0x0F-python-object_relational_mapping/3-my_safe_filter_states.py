#!/usr/bin/python3
''' script that takes in an argument
and display values that are safe from SQL injection '''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    ''' connects to the database '''
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    ''' cursor object '''
    cur = db.cursor()

    ''' SQL Queries execution with cursor object '''
    query = "SELECT * FROM states WHERE name LIKE '{:s}'\
            ORDER BY states.id".format(argv[4])

    cur.execute(query)

    ''' fetch all result '''
    result = cur.fetchall()
    for i in result:
        print(i)
    cur.close()
    db.close()
