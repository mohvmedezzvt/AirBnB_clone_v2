import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_quit(self, mock_stdout):
        self.console.onecmd("help quit")
        expected_output = "Exits the program with formatting\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_EOF(self, mock_stdout):
        self.console.onecmd("help EOF")
        expected_output = "Exits the program without formatting\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_create(self, mock_stdout):
        self.console.onecmd("help create")
        expected_output = "Creates a class of any type\n[Usage]: create <className>\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_show(self, mock_stdout):
        self.console.onecmd("help show")
        expected_output = "Shows an individual instance of a class\n[Usage]: show <className> <objectId>\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_destroy(self, mock_stdout):
        self.console.onecmd("help destroy")
        expected_output = "Destroys an individual instance of a class\n[Usage]: destroy <className> <objectId>\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_all(self, mock_stdout):
        self.console.onecmd("help all")
        expected_output = "Shows all objects, or all of a class\n[Usage]: all <className>\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_count(self, mock_stdout):
        self.console.onecmd("help count")
        expected_output = "Usage: count <class_name>\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_update(self, mock_stdout):
        self.console.onecmd("help update")
        expected_output = "Updates an object with new information\nUsage: update <className> <id> <attName> <attVal>\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            self.assertIn("2f7db327-53d3-4f30-885e-1307d8121c67",
                          mock_stdout.getvalue())

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(
                "show BaseModel 2f7db327-53d3-4f30-885e-1307d8121c67")
            self.assertIn("2f7db327-53d3-4f30-885e-1307d8121c67",
                          mock_stdout.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(
                "destroy BaseModel 2f7db327-53d3-4f30-885e-1307d8121c67")
            self.assertNotIn(
                "2f7db327-53d3-4f30-885e-1307d8121c67", storage.all())

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all BaseModel")
            self.assertIn("2f7db327-53d3-4f30-885e-1307d8121c67",
                          mock_stdout.getvalue())

    def test_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("count BaseModel")
            self.assertIn("1", mock_stdout.getvalue())

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(
                "update BaseModel 2f7db327-53d3-4f30-885e-1307d8121c67 name 'New Name'")
            self.assertIn("'name': 'New Name'", str(
                storage.all()["BaseModel.2f7db327-53d3-4f30-885e-1307d8121c67"]))


if __name__ == '__main__':
    unittest.main()
