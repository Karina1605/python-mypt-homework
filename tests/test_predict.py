import unittest
from add_paths import insert_path
from src.predict import game_core

insert_path()

class TestPredictor(unittest.TestCase):

    def test_game_core_number_lower_than_1_failure(self):
        with self.assertRaises(ValueError):
            game_core(-1)
            
    def test_game_core_number_greater_than_100_failure(self):
        with self.assertRaises(ValueError):
            game_core(1000)

if __name__ == '__main__':
    unittest.main()