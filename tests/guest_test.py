import unittest
from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Luigi", 100)

    def test_guest_has_name_returns_Luigi(self):
        self.assertEqual("Luigi", self.guest.name)

    def test_guest_has_wallet_returns_100(self):
        self.assertEqual(100, self.guest.wallet)
    
    def test_guest_checks_in_returns_1(self):
        room = Room("01")
        room.check_in_guest(self.guest)
        self.assertEqual(1, room.count_guests(room.guests))
    
    def test_guest_checks_out_returns_0(self):
        room = Room("01")
        guest = Guest("Mario", 100)
        room.check_in_guest(guest)
        room.check_out_guest()
        self.assertEqual(0, room.count_guests(room.guests))


        

    