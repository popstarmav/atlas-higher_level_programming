#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql_username> "
              "<mysql_password> <database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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
        # Query State object with the specified name
        state = session.query(State).filter(
            State.name == state_name
        ).one_or_none()

        if state:
            print(state.id)
        else:
            print("Not found")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    main()
