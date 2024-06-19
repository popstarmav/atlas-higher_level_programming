#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # MySQL connection URL
    DB_URL = f"mysql://{mysql_username}:{mysql_password}@localhost:3306/{db_name}"

    # Create the engine
    engine = create_engine(DB_URL)

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        # Query State objects where name contains 'a', order by id ascending
        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

        for state in states_with_a:
            print(f"{state.id}: {state.name}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    main()
