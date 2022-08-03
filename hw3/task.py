"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""

from collections import Counter


def generate_phrase(characters: str, phrase: str) -> bool:
    count_characters = Counter(characters.lower())
    count_phrase = Counter(phrase.lower())

    if len(phrase) > len(characters):
        return False

    for char, cnt in count_phrase.items():

        if char in count_characters and cnt <= count_characters.get(char):
            return True
        else:
            return False


characters = "cbacba"
phrase = "aabbccc"
print(generate_phrase(characters, phrase))

print(generate_phrase('hello', 'olleh'))