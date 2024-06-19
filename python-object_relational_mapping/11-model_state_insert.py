#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <mysql_username> "
              "<mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # MySQL connection URL
    DB_URL = (
        f"mysql://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{db_name}"
    )

    # Create the engine
    engine = create_engine(DB_URL)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        # Create a new State object
        new_state = State(name='Louisiana')

        # Add the new State object to the session
        session.add(new_state)

        # Commit the session to the database
        session.commit()

        # Print the new state's id
        print(new_state.id)

    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        sys.exit(1)

    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    main()
