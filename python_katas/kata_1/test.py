import unittest
from python_katas.kata_1 import questions
from python_katas.utils import unittest_runner



class TestSumOfElements(unittest.TestCase):
    def test_empty_list(self):
        lst = []
        self.assertEqual(questions.sum_of_element(lst), 0)

    def test_single_element(self):
        lst = [5]
        self.assertEqual(questions.sum_of_element(lst), 5)

    def test_multiple_elements(self):
        lst = [1, 2, 3]
        self.assertEqual(questions.sum_of_element(lst), 6)



class TestVerbing(unittest.TestCase):
    """
   ## hello from nofar 1 Katas
    """

    def test_string_longer_than_3_not_include_ing(self):
        word = 'teach'
        self.assertEqual(questions.verbing(word), 'teaching')




class TestWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """
    def test_concatenates_words_with_spaces(self):
        words = ['take', 'me', 'home']
        expected = 'take me home'
        self.assertEqual(questions.words_concatenation(words), expected)


class TestReverseWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """



class TestIsUniqueString(unittest.TestCase):
    """
    2 Katas
    """


class TestListDiff(unittest.TestCase):
    """
    1 Katas
    """



class TestPrimeNumber(unittest.TestCase):
    """
    1 Katas
    """
    def test_is_prime(self):
        num = 2
        expected = True
        self.assertEqual(questions.is_prime(num), expected)
        


class TestPalindromeNum(unittest.TestCase):
    """
    1 Katas
    """


class TestPairMatch(unittest.TestCase):
    """
    3 Katas
    """

class TestBadAverage(unittest.TestCase):
    """
    1 Katas
    """


class TestBestStudent(unittest.TestCase):
    """
    1 Katas
    """


class TestPrintDictAsTable(unittest.TestCase):
    """
    1 Katas
    """

class TestMergeDicts(unittest.TestCase):
    """
    1 Katas
    """


class TestSevenBoom(unittest.TestCase):
    """
    1 Katas
    """

class TestCaesarCipher(unittest.TestCase):
   def test_TestCaesarCipher(self):
        stringx = "Fly Me To The Moon"
        expected = "Iob Ph Wr Wkh Prrq"
        self.assertEqual(questions.caesar_cipher(stringx), expected)


class TestSumOfDigits(unittest.TestCase):
    """
    1 Katas
    """
    def test_sum_of_digits(self):
        nums =("51")
        expected = 6
        self.assertEqual(questions.sum_of_digits(nums), expected)


if __name__ == '__main__':
    import inspect
    import sys

    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
