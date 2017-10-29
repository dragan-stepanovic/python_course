import unittest


class FileParserTests(unittest.TestCase):

    def test_returns_sum_of_all_file_lines(self):
        lines = ['first line', 'second line', 'third line is this']
        lines_count = FileParser().parse(lines)[0]
        self.assertEqual(lines_count, 3)

    def test_returns_number_of_words(self):
        lines = ['first line', 'second line', 'third line is this']
        word_count = FileParser().parse(lines)[1]
        self.assertEqual(word_count, 8)

    def test_returns_number_of_characters(self):
        lines = ['first line', 'second line', 'third line is this']
        char_count = FileParser().parse(lines)[2]
        self.assertEqual(char_count, 39)


class FileParser:
    def parse(self, lines):
        words = [word for line in lines for word in line.split()]
        # same as
        # words = []
        # for line in lines:
        #     for word in line.split():
        #         words.append(word)

        characters = [char for line in lines for char in list(line)]
        # same as
        # characters = []
        # for line in lines:
        #     for character in list(line):
        #         characters.append(character)

        return len(lines), len(words), len(characters)


if __name__ == '__main__':
    unittest.main()
