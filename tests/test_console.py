#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """test the console"""
    def setUp(self):
        """set up for test"""
        FileStorage._FileStorage__objects = {}
        self.mock_stdin = StringIO()
        self.mock_stdout = StringIO()
        self.cli = HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)
        self.cli.prompt = ""
