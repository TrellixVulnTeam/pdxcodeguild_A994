"""
Write a function that quanitifies word occourances in a given string.

>>> quantify_words("Red touching black is a friend of Jack, Red touching yellow can kill a fellow.")
a 2
black 1
can 1
fellow 1
friend 1
is 1
jack 1
kill 1
of 1
red 2
touching 2
yellow 1


>>> quantify_words("In the end, it's concluded that the airspeed velocity of a
(European) unladen swallow is about 24 miles per hour or 11 meters per second.")
(european) 1
11 1
24 1
a 1
about 1
airspeed 1
concluded 1
end 1
hour 1
in 1
is 1
it's 1
meters 1
miles 1
of 1
or 1
per 2
second 1
swallow 1
that 1
the 2
unladen 1
velocity 1
"""

import sys
import re


def quantify_words():
    word_counts = dict()
    question = input("What sentence would you like to quantify? (Leave Blank to Exit) >> ").lower()
    question = question.replace(',', '').replace('.', '').replace('""', '').replace('\n', '')
    # use regex re.sub('\d\w\W*', '') to remove all special characters and digits.
    answer = question.split()

    if question == "":
        sys.exit()

    for word in answer:
        try:
            word_counts[word] += 1
        except KeyError:
            word_counts[word] = 1

    for word, count in sorted(word_counts.items()):
        print(word, count)

    return None


quantify_words()

