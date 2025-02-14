'''
# dice.py

## Objective

Write a simple program that, when run, prompts the user for input then prints a result.

Program should ask the user for the number of dice they want to roll as well as the number of sides per die.

1. Open Atom
1. Create a new file and save it as `dice.py`
1. Follow along with your instructor

------

## Key Concepts

- Variables
- String concatenation
- Handling user input
- Importing functions
- Defining functions
- `for` loops¹
- The `range` statement¹
- Casting values
- Reading error messages

------

Sources:

1. [Compound statements](https://docs.python.org/3/reference/compound_stmts.html)
'''

import random


def dice_roll():
    di_amount = int(input("How many dice are you planning to roll? : "))
    di_sides = int(input("How many sides does each dice have? : "))

    for each_roll in range(di_amount):
        print(random.randint(1, di_sides))

dice_roll()
