import unittest

from classes.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
         self.room = Room("01")

    def test_room_number_01_returns_01(self):
        self.assertEqual("01", self.room.room_number)