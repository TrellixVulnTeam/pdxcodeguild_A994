"""
Write functions that accept 'dirty' string input, and ouputs a human readable value.
Use a combination of python string methods and regular expressions.

Write, test, and refactor as you go.

>>> scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly.')
'Beautiful is better than ugly.'

>>> gentle_clean('Explicit_is-better_than -implicit.')
'Explicit is better than implicit.'

>>> clean_data('  42Simple-is_better_than-compl9ex.   ')
'Simple is better than complex.'

>>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')
'Flat is better than nested.'

>>> mr_clean('Sparse is better than dense')
' S p a r s e   i s   b e t t e r   t h a n   d e n s e '

>>> ms_clean('Readability counts')
'R9y c4s'

>>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly.')
'Errors should never pass silently.'

>>> extracto('1S2pe3cia4l ca5ses ar6en't sp7ecial en8ough to b9reak the r0ules.')
45

>>> extracto('2S4pe6cia8l ca0ses ar2en't sp4ecial en6ough to b8reak the r0ules.')
40

>>> extracto('3S6pe9cia2l ca5ses ar8en't sp1ecial en4ough to b7reak the r0ules.')
45
"""

import re


def scrub_numbers(phrase):
    result = re.sub('\d', '', phrase)
    return result


def gentle_clean(phrase):
    result = re.sub('[\-_]', ' ', phrase).split()
    result = " ".join(result)
    return result


def clean_data(phrase):
    result = re.sub('[\-\s_]', ' ', phrase)
    final_result = re.sub('\d', '', result).strip()
    return final_result


def some_scrubber(phrase):
    '''result = phrase[::2]''' # this is another solution
    result = re.sub('\s\s', ' ', phrase)
    final_result = re.sub('(?<=\w)\s', '', result).rstrip()
    return final_result


def mr_clean(phrase):
    result = phrase.replace('', ' ')
    return result


def ms_clean(phrase):

    def shorten(word):
        return word[0] + str(len(word)-2) + word[-1]

    result = list()
    for word in phrase.split():
        result.append(shorten(word))

    final_result = " ".join(result)
    return final_result


def strong_cleaner(phrase):
    result = re.sub(r'[&@#$*%()!\d]', '', phrase)
    final_result = re.sub(r'(?<=\w)[A-Z]', '', result)
    return final_result


def extracto(phrase):
    extracted = phrase.split()
    first_count = str(len(re.findall('\d', extracted[0])))
    second_number = str(re.findall('\d', extracted[1])[0])
    result = first_count + second_number
    return int(result)