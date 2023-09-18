#!/usr/bin/python3
"""Retrieve and print the State object's id by name from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create an SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object by name and retrieve its id
    state = session.query(State).filter_by(name=state_name).first()

    # Check if a state is found and print its id. If not found, print "Not found."
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
