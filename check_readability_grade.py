# Your program should count the number of letters, words, and sentences in the text. You may assume that a letter is
# any lowercase character from a to z or any uppercase character from A to Z, any sequence of characters separated by
# spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates
# the end of a sentence.

# L is the average number of letters per 100 words in the text, and S is the average number of
# sentences per 100 words in the text. string = input("Please input a text to verify its readability index: ")

import re

string = "A large class of computational problems involve the determination of properties of graphs, digraphs, " \
         "integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other " \
         "countable domains."

LetterCount = len(string.replace('?', '').replace(',', '').replace('.', '').replace(' ', '').replace('!', ''))
# Number of letters
SentenceCount = len(re.split(r'[.!?]+', string)) - 1  # Number of sentences
WordCount = len(string.split())  # Number of words
L = (LetterCount / WordCount) * 100
S = (SentenceCount / WordCount) * 100
index = int(0.0588 * L - 0.296 * S - 15.8)

print(f"Word Count: {WordCount}")
print(f"Sentence Count: {SentenceCount}")
print(f"Letter Count: {LetterCount}")
print(f"L: {L}")
print(f"S: {S}")

if index > 16:
    print(f"Index: Grade 16+")

elif index < 1:
    print(f"Index: Before Grade 1")

else:
    print(f"Index: Grade {index}")
