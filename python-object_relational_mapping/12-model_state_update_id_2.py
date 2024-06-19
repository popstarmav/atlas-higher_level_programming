#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>")
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
        # Query the State object with id = 2
        state_to_update = session.query(State).filter_by(id=2).first()

        if state_to_update:
            # Update the name attribute
            state_to_update.name = 'New Mexico'

            # Commit the session to save changes
            session.commit()

        else:
            print("Not found")

    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        sys.exit(1)

    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    main()
