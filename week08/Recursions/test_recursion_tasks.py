import unittest
from recursion_tasks import deep_find_dfs, deep_find_bfs, deep_find_all_dfs, deep_update


class TestDeepFind(unittest.TestCase):
    def setUp(self):
        self.data = {'a': 1, 'b': 2, 'v':{'c':23, 'b':10, 'k':{'e':4, 'b':1337, 'p':{'mo':'fara', 't': 19}}, 'z': 42, 'o':{'b':999, 'l': 77}}}

    def test_deep_finds_dfs_finds_single_element(self):
        self.assertEqual(deep_find_dfs(self.data, 'c'), 23)

    def test_deep_finds_bfs_finds_single_element(self):
        self.assertEqual(deep_find_bfs(self.data, 'c'), 23)

class TestDeepFindAll(unittest.TestCase):
    def setUp(self):
        self.data = {'a': 1, 'b': 2, 'v':{'c':23, 'b':10, 'k':{'e':4, 'b':1337, 'p':{'mo':'fara', 't': 19}}, 'z': 42, 'o':{'b':999, 'l': 77}}}

    def test_deep_find_all_finds_all_occurances_of_key(self):
        expected_result = [2, 10, 1337, 999]
        self.assertEqual(deep_find_all_dfs(self.data, 'b'),expected_result)

class TestDeepUpdate(unittest.TestCase):
    def setUp(self):
        self.data = {'a': 1, 'b': 2, 'v':{'c':23, 'b':10, 'k':{'e':4, 'b':1337, 'p':{'mo':'fara', 't': 19}}, 'z': 42, 'o':{'b':999, 'l': 77}}}
    
    def test_deep_update_updated_all_occurances_of_a_key(self):
        data_result = deep_update(self.data, 'b', 3)
        expected_keys = [3, 3, 3, 3]
        self.assertEqual(deep_find_all_dfs(data_result, 'b'), expected_keys)

if __name__ == "__main__":
    unittest.main()