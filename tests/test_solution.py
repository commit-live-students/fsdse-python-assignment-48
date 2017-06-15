from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        fpath = "./files/testfile.txt"
        alist = ['apple', 'ball', 'cat', 'dog']
        solution(fpath, alist)

        with open(fpath, 'r') as f:
            text = f.read()
        self.assertEqual(text, 'apple ball cat dog')

