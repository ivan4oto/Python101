import unittest
from Music_library import Song, Playlist

class TestSongClass(unittest.TestCase):
    def test_string_representation(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", duration="3:44")
        result = str(s)
        expectedResult = "Manowar - Odin from The Sons of Odin - 3:44"
        self.assertEqual(result, expectedResult)

    def test_equality_implementation(self):
        s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", duration="3:44")
        s2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", duration="3:44")

        self.assertEqual(s1, s2)

    def test_time_convertion(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", duration="3:44")
        result = s.length(seconds = True)
        self.assertEqual(224, result)


class TestPlaylistClass(unittest.TestCase):
    def test_add_songs(self):
        s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", duration="3:44")
        s2 = Song(title="Doko-Doko", artist="Kondio", album="The Best", duration="3:34")
        s3 = Song(title="Smukacha", artist="Ivana", album="Neznam", duration="3:51")
        p = Playlist('testname')

        
        
        




        
if __name__ == "__main__":
    unittest.main()