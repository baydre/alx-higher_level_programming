#!/usr/bin/python3
''' script that lists all cities from the database '''

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
    query = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC"

    cur.execute(query)

    ''' fetch all result '''
    result = cur.fetchall()
    for i in result:
        print(i)
    cur.close()
    db.close()
