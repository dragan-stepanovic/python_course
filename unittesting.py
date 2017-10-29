import unittest


class FileParserTests(unittest.TestCase):

    def test_returns_sum_of_all_file_lines(self):
        lines = ['first line', 'second line', 'third line']
        lines_count = FileParser().parse(lines)[0]
        self.assertEqual(lines_count, 3)

    def test_returns_number_of_words(self):
        lines = ['first line', 'second line', 'third line is this']
        word_count = FileParser().parse(lines)[1]
        self.assertEqual(word_count, 8)


class FileParser:
    def parse(self, lines):
        words = [word for line in lines for word in line.split()]
        # same as
        # words = []
        # for line in lines:
        #     for word in line.split():
        #         words.append(word)

        return len(lines), len(words)


if __name__ == '__main__':
    unittest.main()
