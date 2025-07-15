def sum_of_element(elements):
    # elements=[1,2]
    sum=0

    for moshe in elements:
        print(moshe)
        sum=sum+moshe

    return sum

def verbing(word):
    string_length = len(word)
    if string_length >= 3:
        if word [-3:] == 'ing':
            word += 'ly'
        else:    
            word += "ing"
    return word

def words_concatenation(words):
    #words_concatenation = ' '.join(words)
    #return words_concatenation

    sentens = " "
    for i in words:
        sentens += i +' '
    return sentens
     
        
def reverse_words_concatenation(words):
    sentens = " "
    for i in words:
        sentens = ' ' + i + sentens
    return sentens

def is_unique_string(some_str):
    seen = set()
    for i in some_str:
        if i in seen:
            return False
        seen.add(i)
    return True

def list_diff(elements):
    if not elements:
        return []
    diff_list = [None]
    
    for i in range(1, len(elements)):
        diff = elements[i] - elements[i - 1]
        diff_list.append(diff)
    
    return diff_list

def prime_number(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def palindrome_num(num):

    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

def pair_match(men, women):
   
    min_diff = float('inf')
    best_pair = (None, None)

    for man_name, man_age in men.items():
        for woman_name, woman_age in women.items():
            diff = abs(man_age - woman_age)
            if diff < min_diff:
                min_diff = diff
                best_pair = (man_name, woman_name)

    return best_pair

def bad_average(a, b, c):
    return (a + b + c) / 3

def best_student(grades):

    best_name = None
    best_grade = float('-inf')
    for name, grades in grades.items():
        if grades > best_grade:
            best_grade = grades
            best_name = name
    return best_name,best_grade

def print_dict_as_table(some_dict):

    print("Key     Value")
    print("-------------")

    for key, value in some_dict.items():
        print(f"{key:<8}{value}")

def merge_dicts(dict1, dict2):

    # dict1.update(dict2)
    for key in dict2:
        dict1[key] = dict2[key]
    return dict1

def seven_boom(n):

    value = []
    for i in range(1, n + 1):
        if i % 7 == 0 or '7' in str(i):
            value.append(i)
    return value


def caesar_cipher(str_to_encrypt):
    """
    2 Kata

    This function encrypts the given string according to caesar cipher (a - d, b - e, ..., y - b, z - c etc...).
    Spaces remain as they are. You can assume the string contain a-z and A-Z chars only.

    e.g.
    Fly Me To The Moon -> Iob Ph Wr Wkh Prrq

    :return:
    """

    encrypted = ""

    for char in str_to_encrypt:
        if char.isalpha():
            shift = 3
            base = ord('A') if char.isupper() else ord('a')

            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted += new_char
        else:
            encrypted += char

    return encrypted

def sum_of_digits(digits_str):
 
    sum = 0
    for char in digits_str:
        sum += int(char)
    return sum

if __name__ == '__main__':

    print('\nsum_of_element:\n--------------------')
    print(sum_of_element([1, 2]))
    print(sum_of_element([1, 3]))
    print(sum_of_element([4, 5, 6]))
    #
    print('\nverbing:\n--------------------')
    print(verbing('walk'))
    print(verbing('swimming'))
    print(verbing('do'))
    #
    print('\nwords_concatenation:\n--------------------')
    print(words_concatenation(['take', 'me', 'home']))
    #
    print('\nreverse_words_concatenation:\n--------------------')
    print(reverse_words_concatenation(['take', 'me', 'home']))
    #
    print('\nis_unique_string:\n--------------------')
    print(is_unique_string('aasdssdsederd'))
    print(is_unique_string('12345tgbnh'))
    #
    print('\nlist_diff:\n--------------------')
    print(list_diff([1, 2, 3, 8, 77, 0]))
    #
    print('\nprime_number:\n--------------------')
    print(prime_number(5))
    print(prime_number(22))
    #
    print('\npalindrome_num:\n--------------------')
    print(palindrome_num(12221))
    print(palindrome_num(577))
    #
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
    # 
    print('\nbad_average:\n--------------------')
    print(bad_average(1, 2, 3))
    #
    print('\nbest_student:\n--------------------')
    print(best_student({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }))
    #
    print('\nprint_dict_as_table:\n--------------------')
    print(print_dict_as_table({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }))
    #
    print('\nmerge_dicts:\n--------------------')
    print(merge_dicts({'a': 1}, {'b': 2}))
    #
    print('\nseven_boom:\n--------------------')
    print(seven_boom(30))
    #
    print('\ncaesar_cipher:\n--------------------')
    print(caesar_cipher('Fly Me To The Moon'))
    #
    print('\nsum_of_digits:\n--------------------')
    print(sum_of_digits('1223432'))


