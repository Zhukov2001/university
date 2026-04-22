from gen_bin_tree import gen_bin_tree
import unittest

class GenBinTree(unittest.TestCase):
    def test_corner_1(self):
        height = 0
        root = 5
        result = gen_bin_tree(height, root)
        self.assertEqual(result, {"5": []})
    
    def test_corner_2(self):
        height = 1
        root = 5
        result = gen_bin_tree(height, root)
        self.assertEqual(result, {"5": [{"6": []}, {"25":[]}]})

    def test_corner_3(self):
        height = 2
        root = 5
        result = gen_bin_tree(height, root)
        self.assertEqual(result,  {"5": [{'6': [{'7': []}, {'36': []}]}, {'25': [{'26': []}, {'625': []}]}]})
    
    def test_corner_4(self):
        height = 3
        root = 5
        result = gen_bin_tree(height, root)
        self.assertEqual(result,  {"5": [{"6": [{'7': [{'8': []}, {'49': []}]}, {'36': [{'37': []}, {'1296': []}]}]}, {"25": [{'26': [{'27': []}, {'676': []}]}, {'625': [{'626': []}, {'390625': []}]}]}]})
    
    def test_corner_5(self):
        height = -1
        root = 5
        result = gen_bin_tree(height, root)
        self.assertEqual(result, None)

    def test_corner_5(self):
        height = int
        root = 5
        result = gen_bin_tree(height, root)
        self.assertEqual(result, None)
if __name__ == '__main__':
    unittest.main()