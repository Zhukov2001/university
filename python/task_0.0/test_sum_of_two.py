from sum_of_two import sum_of_two
import unittest

class TestSumOfTwo(unittest.TestCase):

    # Проверка "штатной" ситуации
    def test_corner_1(self):
        data = [2, 4, 2, 3]
        target = 7
        result = sum_of_two(data, target)
        self.assertEqual(result, [1, 3])
    
    # Проверка с пустым списком
    def test_corner_2(self):
        data = []
        target = 1
        result = sum_of_two(data, target)
        self.assertEqual(result, [])

    # Проверка с "полным" совпадением с целью
    def test_corner_3(self):
        data = [3, 3, 3, 3]
        target = 6
        result = sum_of_two(data, target)
        self.assertEqual(result, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]])

    # Проверка с отсутсвием совпадения с целью
    def test_corner_4(self):
            data = [1, 2, 3, 4]
            target = 100
            result = sum_of_two(data, target)
            self.assertEqual(result, [])

    # Проверка с отрицательным значением в списке
    def test_corner_5(self):
            data = [1, 2, 3, 4, -1]
            target = 3
            result = sum_of_two(data, target)
            self.assertEqual(result, [[0, 1], [3, 5]])

    # Проверка с отрицательной целью
    def test_corner_5(self):
            data = [-1, -2, 3, 4, -1]
            target = -3
            result = sum_of_two(data, target)
            self.assertEqual(result, [[0, 1], [1, 4]])
    

if __name__ == '__main__':
    unittest.main()