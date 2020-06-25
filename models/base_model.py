#!/usr/bin/python3
"""base_model.py module"""
import uuid
import datetime


class BaseModel():
    """
    BaseModel class:
    ----------------
    It defines all common attributes/methods
    for the other classes.

    """

    def __init__(self, id=None):
        """
        This is the constructor.

        Arguments:
        ---------
        id [str] -- UUID generated with python uuid.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()


pedro = BaseModel()
print(pedro.created_at)
print(type(pedro.created_at))
print(pedro.created_at.isoformat())
