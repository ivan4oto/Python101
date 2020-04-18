import unittest
from bowling_game import BowlingGame

class TestBowlingGameClass(unittest.TestCase):
    def test_BowlingGame_raises_error_if_not_enough_frames(self):
        game = BowlingGame([5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6])
        with self.assertRaises(ValueError):
            game.play()

    def test_BowlingGame_raises_error_if_too_much_frames(self):
        game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2, 10, 3, 5])
        with self.assertRaises(ValueError):
            game.play()

    def test_BowlingGame_result_calculates_correctly_strikes_only(self):
        game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        game.play()

        self.assertEqual(game.result(), 300)

    def test_BowlingGame_result_calculates_correctly_open_frames_only(self):
        game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])
        game.play()

        self.assertEqual(game.result(), 65)

    def test_BowlingGame_result_calculates_correctly_spares_only(self):
        game = BowlingGame([3, 7, 6, 4, 2, 8, 9, 1, 1, 9, 5, 5, 4, 6, 2, 8, 9, 1, 3, 7, 5])
        game.play()

        self.assertEqual(game.result(), 146)


if __name__ == "__main__":
    unittest.main()
    