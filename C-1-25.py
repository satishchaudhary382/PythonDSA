# Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For exam-
# ple, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".

import string
def remove_punc(sentence :str) -> str:
    char = []
    for i in sentence:
        if i not in [i for i in string.punctuation]:
            char.append(i)
    print("".join(char))

remove_punc("let's try, Mike. And if there's is anything related to dollar ($) sign then It will remove it. I am sure of it.")

