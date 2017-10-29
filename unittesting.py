import unittest


class FileParserTests(unittest.TestCase):

    def test_returns_sum_of_all_file_lines(self):
        lines = ['first line', 'second line', 'third line']
        count = FileParser().parse(lines)
        self.assertTrue(count == 3)


class FileParser:
    def parse(self, lines):
        return len(lines)


if __name__ == '__main__':
    unittest.main()
