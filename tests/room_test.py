import unittest

from classes.room import Room
from classes.guest import Guest


class TestRoom(unittest.TestCase):

    def setUp(self):
         self.room = Room("01", 2)

    def test_room_number_01_returns_01(self):
        self.assertEqual("01", self.room.room_number)

    def test_more_guests_than_space_returns_No_more_space_available(self):
        room = Room("01", 2)
        guest_01 = Guest("Luigi", 100)
        guest_02 = Guest("Mario", 120)
        guest_03 = Guest("Peach", 150)
        room.check_in_guest(guest_01)
        room.check_in_guest(guest_02)
        room.check_in_guest(guest_03)
        self.assertEqual(False, room.is_enough_space(room.guests))
