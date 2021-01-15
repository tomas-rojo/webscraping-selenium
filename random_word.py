import random

vowels = ['a', 'e', 'i', 'o', 'u']
letters = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


def random_word():
    word = []
    letter_1 = random.choice(letters)
    word.append(letter_1)
    letter_2 = random.choice(vowels)
    word.append(letter_2)
    letter_3 = random.choice(letters)
    word.append(letter_3)
    letter_4 = random.choice(vowels)
    word.append(letter_4)
    letter_5 = random.choice(letters)
    word.append(letter_5)
    word = "".join([str(x) for x in word])
    return word
