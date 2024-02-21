#!/usr/bin/python3
""" """
from datetime import datetime
import json
import os
import unittest
from uuid import UUID

from models.base_model import BaseModel, Base


class TestBasemodel(unittest.TestCase):
    """Represents the tests for the BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
