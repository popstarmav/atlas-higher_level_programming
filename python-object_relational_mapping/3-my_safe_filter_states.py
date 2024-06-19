#!/usr/bin/python3
import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> "
              "<database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
        )

        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
