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
    class TestReverseWordsConcatenation(unittest.TestCase):
     def test_basic(self):
        expected = 'home me take'
        self.assertEqual(questions.reverse_words_concatenation(['take', 'me', 'home']), expected)



class TestIsUniqueString(unittest.TestCase):
    """
    2 Katas
    """
    class TestAllUniqueCharacters(unittest.TestCase):
     def test_all_unique(self):
        self.assertTrue(questions.is_unique_string("abcde"))



class TestListDiff(unittest.TestCase):
    """
    1 Katas
    """
    class TestDiffList(unittest.TestCase):
     def test_regular_list(self):
        expected = [None, 1, 1, 1, 3, 4]
        self.assertEqual(questions.diff_list([1, 2, 3, 4, 7, 11]), expected)



class TestPrimeNumber(unittest.TestCase):
    """
    1 Katas
    """
    def test_is_prime(self):
        num = 2
        expected = True
        self.assertEqual(questions.is_prime(num), expected)



class TestPalindromeNum(unittest.TestCase):

     def test_TestPalindromeNum(self):
        num = 2
        expected = True
        self.assertEqual(questions.pair_match(num), expected)

class TestPairMatch(unittest.TestCase):
    """
    3 Katas
    """
    class TestClosestAgePair(unittest.TestCase):
     def test_basic_match(self):
        men = {"Avi": 30, "Ben": 25}
        women = {"Dana": 24, "Rivka": 29}
        expected = ("Ben", "Dana") 
        self.assertEqual(questions.pair_match(men, women), expected)

    

    
class TestAverage(unittest.TestCase):
    def test_average_integers(self):
        expected = 4.0
        self.assertEqual(questions.bad_average(2, 4, 6), expected)

class TestBestStudent(unittest.TestCase):
    """
    1 Katas
    """

class best_studenttop_student(unittest.TestCase):
    def test_top_student(self):
        grades = {"Ben": 78, "Hen": 88, "Natan": 99, "Efraim": 65, "Rachel": 95}
        expected = "Natan"
        self.assertEqual(questions.best_student(grades),expected)



class TestPrintDictAsTable(unittest.TestCase):

    class TestPrintDict(unittest.TestCase):
     def test_print_dict(self):
        grades = {
            "Ben": 78,
            "Hen": 88,
            "Natan": 99,
            "Efraim": 65,
            "Rachel": 95
        }

        expected_output = (
            "Key\tValue\n"
            "-------------\n"
            "Ben\t78\n"
            "Hen\t88\n"
            "Natan\t99\n"
            "Efraim\t65\n"
            "Rachel\t95\n"
        )
        print(grades)
        self.assertEqual(questions.print_dict_as_table, expected_output)

    """

    ""



class TestMergeDicts(unittest.TestCase):
    """

class TestMergeDicts(unittest.TestCase):
    def test_merge_two_simple_dicts(self):
        d1 = {'a': 1}
        d2 = {'b': 2}
        expected = {'a': 1, 'b': 2}
        self.assertEqual(questions.merge_dicts(d1.copy(), d2.copy()), expected)

    def test_merge_with_overlapping_keys(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 99, 'c': 3}
        expected = {'a': 1, 'b': 99, 'c': 3}
        self.assertEqual(questions.merge_dicts(d1.copy(), d2.copy()), expected)

    def test_merge_empty_dicts(self):
        d1 = {}
        d2 = {}
        expected = {}
        self.assertEqual(questions.merge_dicts(d1, d2), expected)

    def test_merge_with_empty_dict2(self):
        d1 = {'x': 5}
        d2 = {}
        expected = {'x': 5}
        self.assertEqual(questions.merge_dicts(d1.copy(), d2), expected)
    """



class TestSevenBoom(unittest.TestCase):
    """
    class TestSevenBoom(unittest.TestCase):
     def test_SevenBoom(self):
        expected = [7, 14, 17, 21, 27, 28]
        self.assertEqual(questions.seven_boom(30), expected)

    def test_no_boom(self):
        expected = []
        self.assertEqual(questions.seven_boom(6), expected)

    def test_includes_70(self):
        self.assertIn(70, questions.seven_boom(75))

    def test_last_is_77(self):
        expected_last = 77
        self.assertEqual(questions.seven_boom(77)[-1], expected_last)



class TestCaesarCipher(unittest.TestCase):
   def test_TestCaesarCipher(self):
        stringx = "Fly Me To The Moon"
        expected = "Iob Ph Wr Wkh Prrq"
        self.assertEqual(questions.caesar_cipher(stringx), expected)


class TestSumOfDigits(unittest.TestCase):
    ""


    def test_sum_of_digits(self):
        nums =("51")
        expected = 6
        self.assertEqual(questions.sum_of_digits(nums), expected)


if __name__ == '__main__':
    import inspect
    import sys

    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
