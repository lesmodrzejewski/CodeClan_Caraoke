import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Joyride")

    def test_song_has_title_returns_Joyride(self):
        self.assertEqual("Joyride", self.song.title)