#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """Represents the tests for the Place model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tests the type of city_id."""
        new = self.value()
        self.assertEqual(
            type(new.city_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id(self):
        """Tests the type of user_id."""
        new = self.value()
        self.assertEqual(
            type(new.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name(self):
        """Tests the type of name."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_description(self):
        """Tests the type of description."""
        new = self.value()
        self.assertEqual(
            type(new.description),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_rooms(self):
        """Tests the type of number_rooms."""
        new = self.value()
        self.assertEqual(
            type(new.number_rooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_bathrooms(self):
