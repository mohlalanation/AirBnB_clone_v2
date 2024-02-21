#!/usr/bin/python3
""" Module for testing file storage"""
import MySQLdb
import os
import unittest
from datetime import datetime

from models import storage
from models.user import User


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
class TestDBStorage(unittest.TestCase):
    """ Class to test the database storage metho
