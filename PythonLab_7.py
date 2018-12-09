#   Task 2
#  Write a function which returns a sequence of lists of x items each. Lists of less than x items should
#  not be returned.

def list_of_x_items(arr, x):
    if (len(arr) < x or x < 1):
        return []
    return [arr[:x]] + list_of_x_items(arr[x:], x)


print(list_of_x_items(list(range(7)), 3))

#   Task 5
#  Given a string of comma separated integers, write a function which returns a new comma separated
#  string that only contains the numbers which are perfect squares.

from math import sqrt
from functools import reduce

def is_perfect_square(n):
    if (n < 0):
        return False

    i = int(sqrt(n))
    if (n == i*i):
        return True
    else:
        return False

def str_to_int_list(str_of_ints):
    list = str_of_ints.split(',')
    return map(int, list)


def int_list_to_str(int_list):
    return reduce(lambda a, b: str(a) + ',' + str(b), int_list)


def main():
    int_list = str_to_int_list("1,2,3,4,5,6,7,8,9,15,16,18,21,25,42,56,64")
    perfect_squares = filter(is_perfect_square, int_list)
    res = int_list_to_str(perfect_squares)
    print(res)

main()

#   Task 8
#  Write a function which finds all the anagrams in a vector of words. A word x is an anagram of word
#  y if all the letters in x can be rearranged in a different order to form y. Your function should return a
#  set of sets, where each sub-set is a group of words which are anagrams of each other. Each sub-set
#  should have at least two words. Words without any anagrams should not be included in the result.
#  test not run

from itertools import groupby


def find_anagrams(words):
    groups = groupby(sorted(words, key=sorted), sorted)
    return [set(g) for key, g in groups]


print(find_anagrams(['bat', 'rats', 'god', 'tab', 'dog', 'bat', 'cat', 'arts', 'star']))

