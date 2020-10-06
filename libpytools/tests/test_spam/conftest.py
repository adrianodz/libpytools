import pytest
from libpytools.spam.db import Conection

"""
    scope:
    1) fucntion - default
    2) module - run only 1 time for all modules that uses this fixture
    3) session - run only 1 time for a session test
"""


@pytest.fixture(scope='module')
def conection():  # responsible for authenticate the user of DB
    # Setup
    conection_obj = Conection()
    yield Conection()
    # Teardown
    conection_obj.close()


@pytest.fixture
def session(conection):
    # Setup
    session_obj = conection.create_session()  # session is used to manipulate the DB
    yield session_obj
    # Teardown
    session_obj.roll_back()  # destroy all modifications
    session_obj.close()
