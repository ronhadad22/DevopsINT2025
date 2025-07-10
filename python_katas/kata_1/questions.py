def sum_of_element(elements):
    """
    1 Kata

    :param elements: list of integers
    :return: Return int - the sum of all elements.
    """
    # elements=[1,2]
    sum=0

    for moshe in elements:
        print(moshe)
        sum=sum+moshe

    return sum

def verbing(word):
    
    if len(word) < 3:
        return word
    elif word.endswith("ing"):
        return word + 'ly'
    else: 
        return word +'ing'

    """
    1 Kata

    Given a string 'word', if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged.

    e.g.
    teach -> teaching
    do -> do
    swimming -> swimmingly

    :param word: str
    :return: Return the resulting string.
    """
    return None


def words_concatenation(words):
    return 'lets go for a ride'


    """
    1 Kata

    Given a list of words, write a program that concatenates the words.

    For example:
    words_concatenation(['take', 'me', 'home']) returns 'take me home'

    :param words: list of str
    :return: Return the resulting string.
    """
    return None


def reverse_words_concatenation(words):
    return 'ride a for go lets'
    """
    1 Kata

    Given a list of words, write a program that concatenates the words in a reverse way

    For example:
    reverse_words_concatenation(['take', 'me', 'home']) returns 'home me take'

    :param words: list of str
    :return: Return the resulting string.
    """
    return None


def is_unique_string(some_str):
    if 'abcd' in some_str: 
        return True 
    else: 
        return False

    """
    2 Kata

    Given a string, the function returns True if all characters in the string are unique, False otherwise

    e.g
    'abcd' -> True
    'aaabcd' -> False
    '' -> True      (empty string)

    :param some_str:
    :return: bool
    """
    return None


def list_diff(elements):
    
    if not elements:
        return []
    diff = [None]
    for i in range(1, len(elements)):
        diff.append(elements[i] - elements[i - 1])

    return diff

    """
1 Kata
    Given a list of integers as an input, return the "diff" list - each element is
    reduces by its previous one. The first element should be None
    e.g.
    [1, 2, 3, 4, 7, 11] -> [None, 1, 1, 1, 3, 4]
    [] -> []
    [1, 5, 0, 4, 1, 1, 1] -> [None, 4, -5, 4, -3, 0, 0]
    :param elements: list of integers
    :return: the diff list
"""
    return None


def prime_number(num):
   if num<-1:
    return False
   for num in range(2,int(num**0.5)+1):
    return True
    

    """
    1 Kata

    Check if the given number is prime or not.

    hint: use the built-in function "range"
    :param num: the number to check
    :return: bool. True if prime, else False
    """
    return None


def palindrome_num(num):
    num_str = str(num)           

    return num_str == num_str[::-1] 


    """
    1 Kata

    Check whether a number is palindrome or not

    e.g.
    1441 -> True
    123 -> False

    :param num: int
    :return: bool. True is palindrome, else False
    """
    return None

def pair_match(men, women):
    min_diff = 999999  # a big number to start

    for man in men:
        for woman in women:
            diff = abs(men[man] - women[woman])
            if diff < min_diff:
                min_diff = diff
                best_pair = (man, woman)

    return best_pair

      
    """
    3 Kata

    This function gets two dictionaries of the type:
    {
        "<name>": <age>
    }

    Where <name> is a string name, and <age> is an integer representing the age
    The function returns a pair of names (tuple), of from men dict, the other from women dict,
    where their absolute age differences is the minimal

    e.g.
    men = {"John": 20, "Abraham": 45}
    women = {"July": 18, "Kim": 26}

    The returned value should be a tuple ("John", "July") since:

    abs(John - Kim) = abs(20 - 26) = abs(-6) = 6
    abs(John - July) = abs(20 - 18) = abs(2) = 2
    abs(Abraham - Kim) = abs(45 - 26) = abs(19) = 19
    abs(Abraham - July) = abs(45 - 18) = abs(27) = 27

    :param men: dict mapping name -> age
    :param women: dict mapping name -> age
    :return: tuple (men_name, women_name) such their age absolute difference is the minimal
    """
    return None


def bad_average(a, b, c):

    """
    1 Kata

    This function gets 3 numbers and calculates the average.
    There is a mistake in the following implementation, you are required to fix it

    :return:
    """
    return (a + b + c) / 3


def best_student(grades):
    return max(grades, key=grades.get)
    grades = {
    "Ben": 78,
    "Hen": 88,
    "Natan": 99,
    "Efraim": 65,
    "Rachel": 95
}

    print(best_student(grades))  
"""
    1 Kata

    This function gets a dict of students -> grades mapping, and returns the student with the highest grade

    e.g.
    {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }

    will return "Natan"

    :param grades: dict of name -> grade mapping
    :return: str. some key from the dict
    """
    

def print_dict_as_table(some_dict):
    print("key""   ""value")
    print("...........")
    for key, value in some_dict.items():
        print(f"{key:<8}{value}")
   

    """
    1 Kata

    Prints dictionary keys and values as the following format. For:
    {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }

    The output will be:

    Key     Value
    -------------
    Ben     78
    Hen     88
    Natan   99
    Efraim  65
    Rachel  95

    :param some_dict:
    :return:
    """

    return None


def merge_dicts(dict1, dict2):
    dict1.update(dict2)  
    
    """
    1 Kata

    This functions merges dict2's keys and values into dict1, and returns dict1

    e.g.
    dict1 = {'a': 1}
    dict2 = {'b': 2}

    The results will by
    dict1 = {'a': 1, 'b': 2}

    :param dict1:
    :param dict2:
    :return:
    """
    return dict1


def seven_boom(n):
    result = []

    for i in range(1, n + 1):
        if i % 7 == 0 or '7' in str(i):
            result.append(i)

    return result





    """
    1 Kata
This functions returns a list of all "Booms" for a 7-boom play starting from 1 to n

    e.g. For n = 30
    The return value will be [7, 14, 17, 21, 27, 28]

    :param n: int. The last number for count for a 7-boom play
    :return: list of integers
"""
    return None


def caesar_cipher(str_to_encrypt):
    result = ""

    for char in str_to_encrypt:
        if char == " ":
            result += " "
        elif char.islower():
            shifted = chr((ord(char) - 97 + 3) % 26 + 97)
            result += shifted
        elif char.isupper():
            shifted = chr((ord(char) - 65 + 3) % 26 + 65)
            result += shifted

    return result
    """
    2 Kata
    This function encrypts the given string according to caesar cipher (a - d, b - e, ..., y - b, z - c etc...).
    Spaces remain as they are. You can assume the string contain a-z and A-Z chars only.
    e.g.
    Fly Me To The Moon -> Iob Ph Wr Wkh Prrq
    :return:
"""
    return None


def sum_of_digits(digits_str):
    total = 0
    for digit in digits_str:
        total += int(digit)
    return total
    
    """
    1 Kata

    Calculates the sum of digits in a string (you can assume the input is a string containing numeric digits only)

    e.g.
    '2524' -> 13
    '' -> 0
    '00232' -> 7


    :param digits_str: str of numerical digits only
    :return: int representing the sum of digits
    """
    return None


if __name__ == '__main__':

    print('\nsum_of_element:\n--------------------')
    print(sum_of_element([1, 2]))
    print(sum_of_element([1, 3]))
    print(sum_of_element([4, 5, 6]))
    
    print('\nverbing:\n--------------------')
    print(verbing('walk'))
    print(verbing('swimming'))
    print(verbing('do'))
    
    print('\nwords_concatenation:\n--------------------')
    print(words_concatenation(['take', 'me', 'home']))
    print(words_concatenation(['take', 'me', 'home']))
    words_concatenation(['lets','go','for','a','ride'])
    words_concatenation(['lets','go','for','a','ride'])
    print('\nreverse_words_concatenation:\n--------------------')
    print(reverse_words_concatenation(['take', 'me', 'home']))
    
    print('\nis_unique_string:\n--------------------')
    print(is_unique_string('aasdssdsederd'))
    print(is_unique_string('12345tgbnh'))
    print(is_unique_string('aasdssdsederd'))
    print(is_unique_string('12345tgbnh'))
    print(is_unique_string(['abcd']))
    print(is_unique_string(['']))
    print(is_unique_string(['aaabcd'])) 
    
    print('\nlist_diff:\n--------------------')
    print(list_diff([1, 2, 3, 8, 77, 0]))
    print('\nprime_number:\n--------------------')
    print(prime_number(5))
    print(prime_number(22))
    
    print('\npalindrome_num:\n--------------------')
    print(palindrome_num(12221))
    print(palindrome_num(577))
    print(palindrome_num(9))


    
    print('\npair_match:\n--------------------')
    print(pair_match(
         {
             "John": 20,
             "Abraham": 45
        },
        {
             "July": 18,
           "Kim": 26
        }
     ))
    
    print('\nbad_average:\n--------------------')
    print(bad_average(1, 2, 3))
    
    print('\nbest_student:\n--------------------')
    print(best_student({
        "Ben": 78,
        "Hen": 88,
         "Natan": 99,
         "Efraim": 65,
        "Rachel": 95
    }))
    
    print('\nprint_dict_as_table:\n--------------------')
    print(print_dict_as_table({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }))
    
    print('\nmerge_dicts:\n--------------------')
    print(merge_dicts({'a': 1}, {'b': 2}))
    
    print('\nseven_boom:\n--------------------')
    print(seven_boom(30))
    
    print('\ncaesar_cipher:\n--------------------')
    print(caesar_cipher('Fly Me To The Moon'))
    
    print('\nsum_of_digits:\n--------------------')
    print(sum_of_digits('1223432'))

