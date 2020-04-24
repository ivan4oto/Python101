import unittest
import os
from MusicLibrary import Song, Playlist

class TestSongClass(unittest.TestCase):
    def test_song_string_representation_returns_correctly(self):
        s = Song('One', 'U2', 'Achtung Baby', '4:38')
        shouldReturn = 'U2 - One from Achtung Baby - 4:38'

        self.assertEqual(shouldReturn, str(s))

    def test_equal_two_songs_are_equal(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        s2 = Song('One', 'U2', 'Achtung Baby', '4:38')
        
        result = s1 == s2
        self.assertEqual(s1, s2)
        self.assertTrue(result)

    def test_not_equal_songs_aint_equal(self):        
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        s2 = Song('One', 'U3', 'Achtung Baby', '13:37')

        result = s1 != s2
        
        self.assertNotEqual(s1, s2)
        self.assertTrue(result)

    def test_length_returns_length_in_seconds(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        result = s1.song_length(seconds = True)

        self.assertEqual('278', result)

    def test_length_returns_length_in_minutes(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        result = s1.song_length(minutes = True)

        self.assertEqual('4:38', result)

    def test_length_returns_length_in_hours(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        result = s1.song_length(hours = True)

        self.assertEqual('0.08', result)

    def test_length_returns_length_in_minutes_if_given_hours(self):
        s1 = Song('A long song', 'U10', 'Achtung Baby', '2:04:38')
        result = s1.song_length(minutes = True)

        self.assertEqual('124:38', result)

class TestPlaylistClass(unittest.TestCase):
    def test_playlist_add_song(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        p = Playlist('Onesong')
        p.add_song(s1)

        self.assertIn(s1, p.songslist)        


    def test_playlist_add_songs(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        s2 = Song('Warriors of the World', 'Manowar', 'Manowar album', '3:10')
        s3 = Song('Chiki chiki ta', 'Kondio', 'Doko doko', '7:32')
        songlist = [s1, s2, s3]
        p = Playlist('mish mash')
        
        p.add_songs(songlist)

        for s in songlist:
            self.assertIn(s, p.songslist)

        
    def test_playlist_total_length(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        s2 = Song('Warriors of the World', 'Manowar', 'Manowar album', '3:10')
        p = Playlist('random songs')

        p.add_songs([s1,s2])
        result = p.total_length()

        self.assertEqual(result , '7:48')

    def test_show_artists_displays_correctly(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        s2 = Song('Two', 'U2', 'Epimeno', '7:32')
        s3 = Song('Three', 'U2', 'Achtung Baby', '3:15')
        s4 = Song('Warriors of the World', 'Manowar', 'Manowar album', '3:10')
        p = Playlist('Ala bala')
        p.add_songs([s1, s2, s3, s4])
        expectedHistogram = {'U2': 3, 'Manowar': 1}

        self.assertEqual(p.show_artists(), expectedHistogram)

    def test_next_song_returns_next_song(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        s2 = Song('Two', 'U2', 'Epimeno', '7:32')
        p = Playlist('Ala bala')
        p.add_songs([s1, s2])

        self.assertEqual(p.next_song(), s1)
        self.assertEqual(p.next_song(), s2)

    def test_next_song_repeat_works(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        s2 = Song('Two', 'U2', 'Epimeno', '7:32')
        s3 = Song('Three', 'U2', 'Achtung Baby', '3:15')
        p = Playlist('Ala bala', repeat=True)
        p.add_songs([s1, s2, s3])

        self.assertEqual(p.next_song(), s1)
        self.assertEqual(p.next_song(), s2)
        self.assertEqual(p.next_song(), s3)
        self.assertEqual(p.next_song(), s1)

    def test_save(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        s2 = Song('Two', 'U2', 'Epimeno', '7:32')
        p = Playlist('Ala bala')
        p.add_songs([s1, s2])
        p.save()
        self.assertTrue(os.path.isfile('./Ala-bala.json'))

    def test_load(self):
        s1 = Song('One', 'U2', 'Achtung Baby', '4:38')
        s2 = Song('Two', 'U2', 'Epimeno', '7:32')
        s3 = Song('Three', 'Kondio', 'Doko doko', '7:32')
        p = Playlist('newplaylist')
        newsongs = p.load('./Ala-bala.json')
        os.remove("./Ala-bala.json")
        p.add_songs(newsongs)

        self.assertIn(s1, p.songslist)
        self.assertIn(s2, p.songslist)
        self.assertNotIn(s3, p.songslist)

if __name__ == "__main__":
    unittest.main()