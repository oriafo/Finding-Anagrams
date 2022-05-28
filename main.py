# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    first_word = sorted(word)
    second_word = sorted(anagram)
    if first_word == second_word:
        print("True")
        return True
    else:
        print("False")
        return False

find_anagram("hello", "check")
find_anagram("below", "elbow") 
