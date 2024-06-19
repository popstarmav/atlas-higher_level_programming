#!/usr/bin/python3
import sys
import MySQLdb


def main():
    if len(sys.argv) != 4:
        print("Usage: ./0-select_state_update_id_2.py <mysql_username> "
              "<mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
        )

        cursor = db.cursor()
        query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )
        cursor.execute(query)

        cities = cursor.fetchall()

        for city in cities:
            print(city)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
