import unittest
from python_katas.kata_1 import questions
from python_katas.utils import unittest_runner



class TestSumOfElements(unittest.TestCase):
    """
    1 Katas
    """

    def sum_of_element(elements):
        return sum(elements)

    def test_empty_list(self):
        lst = []
        self.assertEqual(questions.sum_of_element(lst), 0)




class TestVerbing(unittest.TestCase):
    """
    1 Katas
    """

    def test_string_longer_than_3_not_include_ing(self):
        word = 'teach'
        self.assertEqual(questions.verbing(word), 'teaching')




class TestWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """




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
    """
    1 Katas
    """


class TestSumOfDigits(unittest.TestCase):
    """
    1 Katas
    """



if __name__ == '__main__':
    import inspect
    import sys

    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
